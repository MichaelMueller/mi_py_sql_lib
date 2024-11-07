# built-in
from typing import Optional, Union, Any, Iterable, Tuple, Dict
import os
# pip
import aiosqlite
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.CreateDatabaseQuery import CreateDatabaseQuery
from ..interfaces.DropDatabaseQuery import DropDatabaseQuery
from ..interfaces.Schema import Schema
from ..interfaces.CreateTableQuery import CreateTableQuery
from ..interfaces.Table import Table
from ..interfaces.Column import Column

class SQLiteDBMS(DBMS):    
    def __init__(self, databases_directory:str, sqlite_ext:str=".sqlite3") -> None:        
        super().__init__()
        self._databases_directory = databases_directory
        self._sqlite_ext = sqlite_ext
                
    # queries   
    # queries   
    def drop_database_query(self, database_name:str) -> DropDatabaseQuery:
        return _SQLiteDropDatabaseQuery( self, database_name )
    
    def create_database_query(self, database_name:str) -> CreateDatabaseQuery: 
        return _SQLiteCreateDatabaseQuery( self, database_name )
    
    async def drop_database(self, database_name:str) -> "DBMS":
        os.remove( database_name )
        return self
    
    # getter
    async def database_names(self) -> list[str]:
        target_extension = self._sqlite_ext.lower()
        filenames = []

        for file in os.listdir(self._databases_directory):
            # Check if the file has the target extension (case insensitive)
            if os.path.isfile( os.path.join( self._databases_directory, file ) ) and file.lower().endswith( target_extension ):
                # Get the filename without extension
                filename_without_extension = os.path.splitext(file)[0]
                filenames.append(filename_without_extension)

        return filenames
    
    async def database_exists(self, database_name:str) -> bool:
        return os.path.exists( self.database_path(database_name) )
    
    async def database(self, database_name:str) -> Database:
        return _SQLiteDatabase(self, database_name)
        
    def database_path( self, database_name:str ) -> "str":
        return f'{self._databases_directory}/{database_name}{self._sqlite_ext}'
    
class _SQLiteDropDatabaseQuery(DropDatabaseQuery):
    def __init__(self, dbms: SQLiteDBMS, database_name:str ) -> None:
        super().__init__()
        self._dbms = dbms
        self._database_name = database_name
        self._if_exits = False
    
    def DBMS(self) -> "DBMS":
        return self._dbms
    
    def if_exists( self, if_exists:bool=True ) -> "DropDatabaseQuery":        
        self._if_exits = if_exists
        return self
            
    async def exec(self) -> None:
        db_path = self._dbms.database_path( self._database_name )
        if self._if_exits and not os.path.exists(db_path):
            return
        os.remove( db_path )

class _SQLiteCreateDatabaseQuery(CreateDatabaseQuery):
    def __init__(self, dbms: SQLiteDBMS, database_name:str ) -> None:
        super().__init__()
        self._dbms = dbms
        self._database_name = database_name
    
    def DBMS(self) -> "DBMS":
        return self._dbms
            
    async def exec(self) -> None:
        db_path = self._dbms.database_path( self._database_name )
        with open(db_path, 'w') as file:
            pass
        return Database()
    
class _SQLiteDatabase(Database):
    def __init__(self, dbms: SQLiteDBMS, database_name:str ) -> None:
        super().__init__()
        self._dbms = dbms
        self._database_name = database_name
    
    def DBMS(self) -> "SQLiteDBMS":
        return self._dbms
                
    def name(self) -> str:
        return self._database_name    
    
    # getter
    async def schema(self) -> Schema:
        return _SQLiteSchema(self)
    # implementation specific

    async def connect(self):
        if self._connection is None:
            db_path = self._dbms.database_path( self._database_name )
            self._connection = await aiosqlite.connect( db_path )

    async def execute_query(self, query, params:Optional[Iterable[Any]]=None):
        await self.connect()  # Make sure the _connection is available
        async with self._connection.execute(query, params or ()) as cursor:
            await self._connection.commit()

    async def close(self):
        if self._connection:
            await self._connection.close()
            self._connection = None   
    
class _SQLiteSchema(Schema):
    def __init__(self, db: _SQLiteDatabase ) -> None:
        super().__init__()
        self._db = db        
        self._connection:aiosqlite.Connection = None
        
    # parent
    def database(self) -> "_SQLiteDatabase":
        return self._db
    
    # queries    
    def create_table_query(self, table_name:str) -> CreateTableQuery: 
        raise NotImplementedError()             
    
    # getter
    def table_names(self) -> list[str]:
        raise NotImplementedError()
    
    def table_exists(self, table_name:str) -> bool:
        raise NotImplementedError()
        
    def tables(self) -> list[Table]:
        raise NotImplementedError()
     
    
class _SQLiteCreateTableQuery(CreateTableQuery):
    def __init__(self, schema: _SQLiteSchema ) -> None:
        super().__init__()
        self._schema = schema
        self._if_not_exists = False
        # per col cached params
        self._cols:Dict[str, dict] = {}
        
    async def exec(self) -> None:
        sqlite_db = self.schema().database()
        sqlite_db.execute_query( self.to_sql() )
    
    def to_sql(self) -> str:
        create_table_sql = f'CREATE TABLE'
        if self._if_not_exists:
            create_table_sql += f' IF NOT EXISTS'
        
        create_table_sql += " (\n"
        
        # inner statements
        inner_sql = []
        params = []
        foreign_keys:Dict[str, Column] = []
        for col_name, col_props in self._cols.items():
            sql = f'{col_name} {col_props["type"]}'
            if col_props["primary_key"]:
                sql += " PRIMARY KEY"
            if col_props["unique"]:
                sql += " UNIQUE"
            if col_props["nullable"] == False:
                sql += " NOT NULL"
            if col_props["default_value"] != None:
                sql += " DEFAULT ?"
                params.append( col_props["default_value"] )
            if col_props["referenced_col"]:
                foreign_keys[col_name] = col_props["referenced_col"]
            inner_sql.append( sql )
            
        for col_name, referenced_col in foreign_keys.items():
            sql = f'FOREIGN KEY ({col_name}) REFERENCES {referenced_col.table().name()}({referenced_col.name()})'
            inner_sql.append( sql )
            
        create_table_sql += ",\n".join( inner_sql )    
                
        create_table_sql += " );"
    
    def schema(self) -> "_SQLiteSchema":
        return self._schema
            
    def int_col(self, 
                name:str, 
                default_value:Optional[int]=None, 
                primary_key:bool=False, 
                unique:Optional[bool]=False, 
                nullable:Optional[bool]=True, 
                referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        col_props = args
        col_props["type"] = "INTEGER"
        return self
    
    def float_col(self, 
                  name:str, 
                  default_value:Union[float, None]=None, 
                  primary_key:bool=False, 
                  unique:Optional[bool]=False, 
                  nullable:Optional[bool]=True, 
                  referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        col_props = args
        col_props["type"] = "FLOAT"
        return self
        
    def string_col(self, 
                   name:str, 
                   max_length:int, 
                   default_value:Union[str, None]=None, 
                   primary_key:bool=False, 
                   unique:Optional[bool]=False, 
                   nullable:Optional[bool]=True, 
                   referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        del args["max_length"]
        col_props = args
        col_props["type"] = "TEXT"
        return self
    
    def int_primary_key_col(self, 
                            name:str, 
                            auto_increment:Optional[bool]=True) -> "CreateTableQuery":
        
        self.int_col(name, primary_key=True)    
        self._cols[name]["auto_increment"] = auto_increment
        return self
    
    
    def if_not_exists( self, if_not_exists:bool=True ) -> "CreateTableQuery":
        self._if_not_exists = if_not_exists
        return self
    
            