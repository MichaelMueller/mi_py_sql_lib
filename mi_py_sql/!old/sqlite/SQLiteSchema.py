# built-in
from typing import TYPE_CHECKING, Dict, Optional, Any
# pip
# local
from ..interfaces.CreateTable import CreateTable
from ..interfaces.Schema import Schema
from ..interfaces.Table import Table

from .SQLiteCreateTable import SQLiteCreateTable
if TYPE_CHECKING:
    from .SQLiteDatabase import SQLiteDatabase                    

class SQLiteSchema(Schema):
    def __init__(self, db: "SQLiteDatabase" ) -> None:
        super().__init__()
        self._db = db  
        
    # parent
    def database(self) -> "SQLiteDatabase":
        return self._db
    
    # table management (Schema interface)
    def create_table_query(self, table_name:str) -> CreateTable: 
        return SQLiteCreateTable(self, table_name)             
                    
    async def table(self, name:str) -> Table:
        raise NotImplementedError()
    
    async def table_names(self) -> list[str]:
        tables = await self._db.fetch_all( "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';" )
        table_names = [table[0] for table in tables]
        return table_names
    
    async def rename_table(self, name:str, new_name:str) -> "Schema": 
        raise NotImplementedError()
    
    async def drop_table(self, name:str) -> "Schema": 
        raise NotImplementedError()
        