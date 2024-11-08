# built-in imports
from typing import Any, Union, Optional

# local imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Schema import Schema
    
from .SqlQuery import SqlQuery
from .Column import Column
from .Table import Table

class CreateTable(SqlQuery):
    """ fluent interface for creating a table """
     
    async def exec(self) -> Table:
        raise NotImplementedError()
            
    def column( self, name:str, type_:Union[str, int, float, bytes] ) -> "CreateTable":
        raise NotImplementedError()
    
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