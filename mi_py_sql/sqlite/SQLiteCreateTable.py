
# built-in
from typing import TYPE_CHECKING, Iterable, Optional, Any, Union, Tuple
# pip
import aiosqlite
# local
from ..interfaces.Database import Database
from ..interfaces.CreateTable import CreateTable
from ..interfaces.Table import Table
from .SQLiteSchema import SQLiteSchema
if TYPE_CHECKING:
    from .SQLiteSchema import SQLiteSchema
    
class SQLiteCreateTable(CreateTable):
    def __init__(self, schema: "SQLiteSchema" ) -> None:
        super().__init__()
        self._schema = schema
        self._col_data = {}
        self._cur_col = None
    
    # SqlQuery interface
    def to_sql(self) -> Tuple[str, Iterable[Any]]:
        raise NotImplementedError()
    
    # CreateTable interface    
    async def exec(self) -> Table:
        raise NotImplementedError()
            
    def column( self, name:str, type_:Union[str, int, float, bytes] ) -> "CreateTable":
        if not name in self._col_data:
            self._col_data[name] = { "name": name, "type": type_ }
    
    def integer(self ) -> "CreateTable":
        raise NotImplementedError()
    
    def integer_auto_pk( self ) -> "CreateTable":
        raise NotImplementedError()
    
    def float_( self ) -> "CreateTable":        
        raise NotImplementedError()
    
    def string( self, max_length:int ) -> "CreateTable":
        raise NotImplementedError()
    
    def blob( self, max_length:int ) -> "CreateTable":
        raise NotImplementedError()
    
    def default_value( self, default_value:Union[int, float, str, bytes, None]=None ) -> "CreateTable":
        raise NotImplementedError()
            
    def unique( self ) -> "CreateTable":        
        raise NotImplementedError()
    
    def primary_key( self ) -> "CreateTable":        
        raise NotImplementedError()
    
    def references( self, c:Column ) -> "CreateTable":        
        raise NotImplementedError()