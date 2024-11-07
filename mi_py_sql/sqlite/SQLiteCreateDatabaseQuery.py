
# built-in
from typing import TYPE_CHECKING
import os
# pip
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.CreateDatabaseQuery import CreateDatabaseQuery

if TYPE_CHECKING:
    from .SQLiteDBMS import SQLiteDBMS
    
class SQLiteCreateDatabaseQuery(CreateDatabaseQuery):
    def __init__(self, dbms: "SQLiteDBMS", database_name:str ) -> None:
        super().__init__()
        self._dbms = dbms
        self._database_name = database_name
    
    def DBMS(self) -> "DBMS":
        return self._dbms
            
    async def exec(self) -> None:
        db_path = self._dbms.database_path( self._database_name )
        with open(db_path, 'w') as file:
            pass
        return await self._dbms.database(self._database_name)