
# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any, Union
# pip
import aiosqlite
# local
from ..interfaces.Table import Table
from ..interfaces.Schema import Schema
from ..interfaces.Column import Column
from .SQLiteColumn import SQLiteColumn

if TYPE_CHECKING:    
    from .SQLiteSchema import SQLiteSchema
    
class SQLiteTable(Table):
    def __init__(self, schema:"SQLiteSchema", name:str ) -> None:
        super().__init__()
        self._schema = schema
        self._name = name        
            
    # Table interface
    def schema(self) -> "Schema":
        return self._schema
    
    def name(self) -> str:
        return self._name
    
    # column management
    async def column_names(self) -> list[str]:
        column_names = [info[1] for info in await self._table_info()]
        return column_names
        
    async def column(self, name:str) -> Union[None, Column]:       
        for sqlite_col_info in await self._table_info():
            if sqlite_col_info[1] == name:
                return SQLiteColumn( self, sqlite_col_info )        
        return None    
        
    async def _table_info(self) -> list:        
        return self._schema.database().fetch_all( f"PRAGMA table_info({self._name})" )
    
    #     for sqlite_col_info in await self._table_info():
    #         if sqlite_col_info[1] == name:
    #             _, name, col_type, notnull, dflt_value, pk = sqlite_col_info
    #             type_map = {"integer": int, "text": str, "real": float, "blob": bytes}
    #             col_props = {
    #                 "table": self,
    #                 "name": name,
    #                 "type": type_map[ col_type.lower() ],
    #                 "is_primary_key": pk == 1,
    #                 "is_unique": self._is_column_unique(name),
    #                 "is_nullable": notnull == 0,
    #                 "is_auto_increment": col_type.lower() == "integer" and pk == 1,
    #                 "max_length": None,
    #                 "max_length": None,
    #                 "max_length": None,
    #             }
    #             return StdColumn()
    
    # async def _is_column_unique( self, column_name:str ) -> bool:
    #     # Get all indexes on the table
    #     indexes = self._schema.database().fetch_all(f"PRAGMA index_list('{self._name}')")

    #     # Check each index to see if it's unique and includes the specified column
    #     is_column_unique = False
    #     for index in indexes:
    #         index_name, unique = index[1], index[2]
    #         if unique:  # If the index is unique
    #             # Get the columns in this unique index                
    #             index_list = self._schema.database().fetch_all(f"PRAGMA index_info('{index_name}')")
    #             indexed_columns = [column_info[2] for column_info in index_list]
    #             if column_name in indexed_columns:
    #                 is_column_unique = True
    #                 break
    
  
        