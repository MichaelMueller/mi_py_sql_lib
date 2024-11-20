# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING
import asyncio
# pip
import aiosqlite
# local imports
from mi_py_sql import Database

class SqliteDatabase(Database):
    """SQLite database class that keeps the connection open."""
    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._connection = None

    async def connect(self) -> aiosqlite.Connection:
        """Open a connection to the SQLite database."""
        self._connection = await aiosqlite.connect(self.db_path)

    async def close(self):
        """Close the SQLite database connection."""
        if self._connection:
            await self._connection.close()
            self._connection = None

    async def execute(self, query: str, params: tuple = ()):
        """Execute a query asynchronously."""
        connection = await self.connect()
        async with connection.execute(query, params) as cursor:
            return await cursor.fetchall()

    async def execute_write(self, query: str, params: tuple = ()):
        """Execute a write query asynchronously."""
        connection = await self.connect()
        async with connection.execute(query, params):
            return await connection.commit()

    def __del__(self):
        """Destructor to ensure the connection is closed."""
        if self._connection:
            # Since destructors cannot be async, you must warn about manual cleanup.
            print("Warning: Connection was not closed explicitly.")
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(self.close())
            else:
                loop.run_until_complete(self.close())