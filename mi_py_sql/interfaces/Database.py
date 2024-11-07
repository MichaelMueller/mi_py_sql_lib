# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .DBMS import DBMS
    
# other imports
from .Schema import Schema

class Database:
    
    # parent
    def DBMS(self) -> "DBMS":
        raise NotImplementedError()
    
    # getter
    async def schema(self) -> Schema:
        raise NotImplementedError()
    
    def name(self) -> str:
        raise NotImplementedError()
    