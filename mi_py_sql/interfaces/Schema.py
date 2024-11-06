# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Database import Database
    
# other imports
from .Table import Table

class Schema:
    
    def database(self) -> "Database":
        pass
    
    def tables(self) ->  list[Table]:
        pass