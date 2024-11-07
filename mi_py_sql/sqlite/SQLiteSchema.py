# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any
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
        
    # parent
    def database(self) -> "SQLiteDatabase":
        return self._db
    
    # queries    
    def create_table_query(self, table_name:str) -> CreateTableQuery: 
        return SQLiteCreateTableQuery(self, table_name)             
    
    # getter
    def table_names(self) -> list[str]:
        raise NotImplementedError()
    
    def table_exists(self, table_name:str) -> bool:
        raise NotImplementedError()
        
    def tables(self) -> list[Table]:
        raise NotImplementedError()