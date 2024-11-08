
# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any, Union
# pip
import aiosqlite
# local
from ..interfaces.Table import Table
from ..interfaces.Column import Column
if TYPE_CHECKING:
    from .SQLiteTable import SQLiteTable
    
class SQLiteColumn(Column):
    def __init__(self, table:"SQLiteTable", sqlite_col_info:dict ) -> None:
        super().__init__()
        self._table = table
        
        # set internal props
        _, name, col_type, notnull, dflt_value, pk = sqlite_col_info        
        type_map = {"integer": int, "text": str, "real": float, "blob": bytes}  
        
        self._name = name               
        self._type = type_map[ col_type.lower() ]
        self._is_primary_key = pk == 1               
        self._is_nullable = notnull == 0
        self._is_auto_increment = pk == 1 and self._is_primary_key                  
        self._dflt_value = dflt_value
        
    def table(self) -> "Table":
        return self._table
    
    def name(self) -> str:
        return self._name
    
    async def type_(self) -> Union[str, int, float, bytes]:
        return self._type
    
    async def is_primary_key( self ) -> bool:
        return self._is_primary_key
    
    async def is_unique( self ) -> bool:
        raise NotImplementedError()
    
    async def is_nullable( self ) -> bool:
        return self._is_nullable
        
    async def is_auto_increment( self ) -> bool:
        return self._is_auto_increment
    
    async def max_length( self ) -> Union[int, None]:
        return None
    
    async def default_value( self ) -> Union[int, float, str, bytes, None]:
        return self._dflt_value
    
    async def referenced_column( self ) -> Union["Column", None]:
        raise NotImplementedError()