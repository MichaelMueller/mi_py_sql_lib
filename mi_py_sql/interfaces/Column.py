# forward declerations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    from .Table import Table

class Column:
    
    def table(self) -> "Table":
        raise NotImplementedError()
    
    def name(self) -> str:
        raise NotImplementedError()
    
    def is_primary_key( self ) -> bool:
        raise NotImplementedError()
    
    def is_unique( self ) -> bool:
        raise NotImplementedError()
    
    def is_nullable( self ) -> bool:
        raise NotImplementedError()
    
    def referenced_col( self ) -> Union["Column", None]:
        raise NotImplementedError()