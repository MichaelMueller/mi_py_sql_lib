# built-in
import os
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.CreateDatabaseQuery import CreateDatabaseQuery
from ..interfaces.DropDatabaseQuery import DropDatabaseQuery

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
        raise NotImplementedError()
        
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