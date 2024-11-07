
# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any
# pip
import aiosqlite
# local
from ..interfaces.Database import Database
from ..interfaces.Schema import Schema
from .SQLiteSchema import SQLiteSchema
if TYPE_CHECKING:
    from .SQLiteDBMS import SQLiteDBMS
    
class SQLiteDatabase(Database):
    def __init__(self, dbms: "SQLiteDBMS", database_name:str ) -> None:
        super().__init__()
        self._dbms = dbms
        self._database_name = database_name
        self._connection:aiosqlite.Connection = None
    
    def DBMS(self) -> "SQLiteDBMS":
        return self._dbms
                
    def name(self) -> str:
        return self._database_name    
    
    # getter
    async def schema(self) -> Schema:
        return SQLiteSchema(self)
    # implementation specific

    async def connect(self):
        if self._connection is None:
            db_path = self._dbms.database_path( self._database_name )
            self._connection = await aiosqlite.connect( db_path )

    async def execute_query(self, query, params:Optional[Iterable[Any]]=None):
        await self.connect()  # Make sure the _connection is available
        async with self._connection.execute(query, params or ()):
            await self._connection.commit()

    async def close(self):
        if self._connection:
            await self._connection.close()
            self._connection = None   