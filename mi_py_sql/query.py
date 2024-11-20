from typing import Tuple, Any, Iterable, TypedDict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from mi_py_sql import Database

class Query:
    
    def __init__(self, database:"Database") -> None:
        super().__init__()
        self._database = database
        
    def database(self) -> "Database":
        return self._database 
        
    async def exec( self, args:Iterable[Any] ) -> Any:
        return await self.database().exec( self, args )
    
    def to_sql( self ) -> str:
        raise NotImplementedError()
    