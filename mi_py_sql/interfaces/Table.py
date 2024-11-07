# forward declerations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    from .Schema import Schema
    
# other imports
from .Column import Column

class Table:
    
    # parent
    def schema(self) -> "Schema":
        pass
    
    # queries   
    
    # getter
    def name(self) -> str:
        raise NotImplementedError()
    
    def column_names(self) -> list[str]:
        raise NotImplementedError()
    
    def column_exists(self, name:str) -> bool:
        raise NotImplementedError()
    
    def column(self, name:str) -> Column:
        raise NotImplementedError()
    
    def autoincrement_column( self ) -> Union[str, None]:
        raise NotImplementedError()