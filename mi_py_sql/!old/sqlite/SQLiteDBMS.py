# built-in
from typing import Dict, Optional, Union
import os
# pip
import aiosqlite
import aiofiles.os
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
# local same hierarchy
from .SQLiteDatabase import SQLiteDatabase

class SQLiteDBMS(DBMS):    
    def __init__(self, databases_directory:str, sqlite_ext:str=".sqlite3") -> None:        
        super().__init__()
        self._databases_directory = databases_directory
        self._sqlite_ext = sqlite_ext
        self._databases:Dict[str, SQLiteDatabase] = {}
                
    async def database(self, database_name:str, create:Optional[bool]=False) -> Union[None, Database]: 
        db_path = self.database_path( database_name )        
        if database_name not in self._databases:
            # check if db could be loaded or create an empty file if create is True
            exists_on_disk = await aiofiles.os.path.exists(db_path)
            if not exists_on_disk and create:                
                async with aiofiles.open(db_path, 'w'):
                    exists_on_disk = True
            # finally add it to my set of opened databases
            if exists_on_disk:            
                self._databases[database_name] = SQLiteDatabase(self, database_name)
        return self._databases[database_name] if database_name in self._databases else None
    
    async def database_names(self) -> list[str]:
        target_extension = self._sqlite_ext.lower()
        filenames = []
        for file in await aiofiles.os.listdir(self._databases_directory):
            # Check if the file has the target extension (case insensitive)
            if file.lower().endswith( target_extension ):                
                filename_without_extension = os.path.splitext(file)[0]
                filenames.append(filename_without_extension)
        return filenames
    
    async def drop_database(self, database_name:str) -> "SQLiteDBMS":
        db_path = self.database_path( database_name )
        
        loaded = database_name in self._databases
        exists = False
        if loaded:
            self._databases[database_name].close()
            del self._databases[database_name]
        else:            
            exists = await aiofiles.os.path.exists( db_path )
            
        if loaded or exists:
            await aiofiles.os.remove( db_path )
            
        return self
    
    async def close_all(self) -> None:
        for database in self._databases.values():
            await database.close()
    
    # implementation specific        
    def database_path( self, database_name:str ) -> "str":
        return f'{self._databases_directory}/{database_name}{self._sqlite_ext}'
    

     