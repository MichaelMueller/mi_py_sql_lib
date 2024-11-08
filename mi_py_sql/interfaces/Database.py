# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .DBMS import DBMS
    
# other imports
from .Schema import Schema
from .CreateTable import CreateTable

class Database:
    
    # parent
    def DBMS(self) -> "DBMS":
        raise NotImplementedError()
    
    def schema(self) -> Schema: # will load the complete schema of this DB as is
        raise NotImplementedError()
    
    def name(self) -> str:
        raise NotImplementedError()      