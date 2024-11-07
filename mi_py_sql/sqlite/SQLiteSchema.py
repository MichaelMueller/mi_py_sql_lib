# built-in
from typing import TYPE_CHECKING, Dict, Optional, Any
# pip
# local
from ..interfaces.CreateTableQuery import CreateTableQuery
from ..interfaces.Schema import Schema
from ..interfaces.Table import Table

from .SQLiteCreateTableQuery import SQLiteCreateTableQuery
if TYPE_CHECKING:
    from .SQLiteDatabase import SQLiteDatabase                    

class SQLiteSchema(Schema):
    def __init__(self, db: "SQLiteDatabase" ) -> None:
        super().__init__()
        self._db = db  
        self._tables:Dict[str, Table] = {}
        
    # parent
    def database(self) -> "SQLiteDatabase":
        return self._db
    
    # queries    
    def create_table_query(self, table_name:str) -> CreateTableQuery: 
        return SQLiteCreateTableQuery(self, table_name)             
    
    # getter
    async def table_names(self) -> list[str]:
        tables = await self._db.fetch_all( "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';" )
        table_names = [table[0] for table in tables]
        return table_names
        
    async def table_exists(self, table_name:str) -> bool:
        return table_name in await self.table_names()
        
    async def table(self, name:str) -> Table:
        raise NotImplementedError()
        