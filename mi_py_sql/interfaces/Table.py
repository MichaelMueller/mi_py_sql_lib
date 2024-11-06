# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Schema import Schema
    
# other imports
from .Column import Column

class Table:
    
    def schema(self) -> "Schema":
        pass
    
    def columns(self) ->  list[Column]:
        pass