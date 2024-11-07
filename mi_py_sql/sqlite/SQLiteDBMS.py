# built-in
from typing import Dict
import os
# pip
import aiosqlite
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.CreateDatabaseQuery import CreateDatabaseQuery
from ..interfaces.DropDatabaseQuery import DropDatabaseQuery

from .SQLiteDatabase import SQLiteDatabase
from .SQLiteDropDatabaseQuery import SQLiteDropDatabaseQuery
from .SQLiteCreateDatabaseQuery import SQLiteCreateDatabaseQuery

class SQLiteDBMS(DBMS):    
    def __init__(self, databases_directory:str, sqlite_ext:str=".sqlite3") -> None:        
        super().__init__()
        self._databases_directory = databases_directory
        self._sqlite_ext = sqlite_ext
        self._databases:Dict[str, SQLiteDatabase] = {}
                
    # other
    async def disconnect(self) -> None:
        for database in self._databases.values():
            await database.close()
    
    # queries   
    def drop_database_query(self, database_name:str) -> DropDatabaseQuery:
        return SQLiteDropDatabaseQuery( self, database_name )
    
    def create_database_query(self, database_name:str) -> CreateDatabaseQuery: 
        return SQLiteCreateDatabaseQuery( self, database_name )
    
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
        if not database_name in self._databases:
            self._databases[database_name] = SQLiteDatabase(self, database_name)
        return self._databases[database_name]
        
    def database_path( self, database_name:str ) -> "str":
        return f'{self._databases_directory}/{database_name}{self._sqlite_ext}'
    

     