# built-in imports
from typing import Any

# local imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .DBMS import DBMS
    
from .Query import Query
from .Database import Database

class CreateDatabaseQuery(Query): 
    
    def DBMS(self) -> "DBMS":
        raise NotImplementedError()
        
    async def exec(self) -> Database:
        raise NotImplementedError()