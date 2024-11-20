# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING
import asyncio, logging
# pip
import aiosqlite
# local imports
from .database import Database
from .sqlite_create_table import SqliteCreateTable
from .sqlite_rename_table import SqliteRenameTable
from .sqlite_drop_table import SqliteDropTable

class SqliteDatabase(Database):
    """SQLite database class that keeps the connection open."""
    def __init__(self, db_path: str):
        super().__init__()
        self._db_path = db_path
        # self._connection = None

    def path(self) -> str:
        return self._db_path
    
    def create_table(self, name:str) -> SqliteCreateTable:
        return SqliteCreateTable(self, name) 
    
    def rename_table(self, name:str) -> SqliteRenameTable:
        return SqliteRenameTable(self, name) 

    def drop_table(self, name:str) -> SqliteDropTable:
        return SqliteDropTable(self, name) 
    
    async def execute(self, query: str, params: tuple = ()):
        """Execute a query asynchronously."""
        async with aiosqlite.connect( self.path() ) as db:
            async with db.execute(query, params) as cursor:
                return await cursor.fetchall()

    async def execute_write(self, query: str, params: tuple = ()):
        """Execute a write query asynchronously."""
        async with aiosqlite.connect( self.path() ) as db:
            async with db.execute(query, params):
                return await db.commit()
    
    # async def connect(self) -> aiosqlite.Connection:
    #     """Open a connection to the SQLite database."""
    #     if self._connection == None:
    #         self._connection = await aiosqlite.connect(self._db_path)
    #     return self._connection

    # async def disconnect(self) -> "SqliteDatabase":
    #     """Close the SQLite database connection."""
    #     if self._connection:
    #         await self._connection.close()
    #         self._connection = None
    #     return self
    
    # def disconnect_synced( self ) -> Union[None, asyncio.Task]:        
    #     if self._connection:
    #         # Since destructors cannot be async, you must warn about manual cleanup.
    #         loop = asyncio.get_event_loop()
    #         if loop.is_running():
    #             return asyncio.create_task(self.disconnect())
    #         else:
    #             loop.run_until_complete(self.disconnect())
    #             return None

    # def __del__(self):
    #     """Destructor to ensure the connection is closed."""
    #     print("destructor")
    #     if self._connection:            
    #         logging.warning("Warning: Connection was not closed explicitly.")
    #         self.disconnect_synced()