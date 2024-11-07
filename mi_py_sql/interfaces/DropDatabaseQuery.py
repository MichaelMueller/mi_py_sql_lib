# built-in imports
from typing import Any

# local imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .DBMS import DBMS
    
from .Query import Query

class DropDatabaseQuery(Query): 
    
    def DBMS(self) -> "DBMS":
        raise NotImplementedError()
    
    def if_exists( self, if_exists:bool=True ) -> "DropDatabaseQuery":
        raise NotImplementedError()
            
    async def exec(self) -> None:
        raise NotImplementedError()