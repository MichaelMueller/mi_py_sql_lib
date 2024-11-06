# built-in
import os
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database

class SQLiteDBMS(DBMS):    
    def __init__(self, databases_directory:str, sqlite_ext:str=".sqlite3") -> None:        
        super().__init__()
        self._databases_directory = databases_directory
        self._sqlite_ext = sqlite_ext
                
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
        return os.path.exists( self._database_path(database_name) )
    
    async def database(self, database_name:str) -> Database:
        raise NotImplementedError()
    
    async def drop_database(self, database_name:str) -> "DBMS":
        os.remove( database_name )
        return self
    
    def _database_path( self, database_name:str ) -> "str":
        return f'{self._databases_directory}/{database_name}{self._sqlite_ext}'