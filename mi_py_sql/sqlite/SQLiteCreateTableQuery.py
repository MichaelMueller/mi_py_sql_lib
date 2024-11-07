# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any, Dict, Tuple, Union
# pip
# local
from ..interfaces.CreateTableQuery import CreateTableQuery
from ..interfaces.Column import Column

if TYPE_CHECKING:
    from .SQLiteSchema import SQLiteSchema    

class SQLiteCreateTableQuery(CreateTableQuery):
    def __init__(self, schema: "SQLiteSchema", table_name:str ) -> None:
        super().__init__()
        self._schema = schema
        self._table_name = table_name
        self._if_not_exists = False
        # per col cached params
        self._cols:Dict[str, dict] = {}
        
    async def exec(self) -> None:
        sqlite_db = self.schema().database()
        sql, params = self.to_sql()
        await sqlite_db.execute_query( sql, params )
    
    def to_sql(self) -> Tuple[str, Iterable[Any]]:
        create_table_sql = f'CREATE TABLE {self._table_name}'
        if self._if_not_exists:
            create_table_sql += f' IF NOT EXISTS'
        
        create_table_sql += " (\n"
        
        # inner statements
        inner_sql = []
        params = []
        foreign_keys:Dict[str, Column] = {}
        for col_name, col_props in self._cols.items():
            sql = f'{col_name} {col_props["type"]}'
            if col_props["primary_key"]:
                sql += " PRIMARY KEY"
            if col_props["unique"]:
                sql += " UNIQUE"
            if col_props["nullable"] == False:
                sql += " NOT NULL"
            if col_props["default_value"] != None:
                sql += f' DEFAULT'
                if type( col_props["default_value"] ) == str:
                    sql += f' "{col_props["default_value"]}"'
                else:                    
                    sql += f' {col_props["default_value"]}'
            if col_props["referenced_col"]:
                foreign_keys[col_name] = col_props["referenced_col"]
            inner_sql.append( sql )
            
        for col_name, referenced_col in foreign_keys.items():
            sql = f'FOREIGN KEY ({col_name}) REFERENCES {referenced_col.table().name()}({referenced_col.name()})'
            inner_sql.append( sql )
            
        create_table_sql += ",\n".join( inner_sql )    
                
        create_table_sql += " );"
        
        return (create_table_sql, params)
    
    def schema(self) -> "SQLiteSchema":
        return self._schema
            
    def int_col(self, 
                name:str, 
                default_value:Optional[int]=None, 
                primary_key:bool=False, 
                unique:Optional[bool]=False, 
                nullable:Optional[bool]=False, 
                referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        col_props = args
        col_props["type"] = "INTEGER"
        self._cols[name] = col_props
        return self
    
    def float_col(self, 
                  name:str, 
                  default_value:Union[float, None]=None, 
                  primary_key:bool=False, 
                  unique:Optional[bool]=False, 
                  nullable:Optional[bool]=False, 
                  referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        col_props = args
        col_props["type"] = "FLOAT"
        self._cols[name] = col_props
        return self
        
    def string_col(self, 
                   name:str, 
                   max_length:int, 
                   default_value:Union[str, None]=None, 
                   primary_key:bool=False, 
                   unique:Optional[bool]=False, 
                   nullable:Optional[bool]=False, 
                   referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        args = locals()
        del args["self"]
        del args["name"]
        del args["max_length"]
        col_props = args
        col_props["type"] = "TEXT"
        self._cols[name] = col_props
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
    
            