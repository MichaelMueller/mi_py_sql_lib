# built-in
from typing import TYPE_CHECKING
import os
# pip
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.DropDatabaseQuery import DropDatabaseQuery

if TYPE_CHECKING:
    from .SQLiteDBMS import SQLiteDBMS

class SQLiteDropDatabaseQuery(DropDatabaseQuery):
    def __init__(self, dbms: "SQLiteDBMS", database_name:str ) -> None:
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