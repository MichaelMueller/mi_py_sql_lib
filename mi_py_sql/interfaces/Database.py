# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .DBMS import DBMS
    
# other imports
from .Schema import Schema

class Database:
    
    def DBMS(self) -> "DBMS":
        pass
    
    def schema(self) -> Schema:
        pass
    
    def name(self) -> str:
        pass