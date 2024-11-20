from typing import Tuple, Any, Iterable, TypedDict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from mi_py_sql import Database

class Query:
    
    def __init__(self, database:"Database") -> None:
        super().__init__()
        self._database = database
        
    def database(self) -> "Database":
        return self._database 
        
    async def exec( self ) -> Any:
        return await self.database().exec( self )
    
    def to_sql( self ) -> Tuple[str, Iterable[Any]]:
        raise NotImplementedError()
    
    def args( self ) -> Iterable[Any]:
        raise NotImplementedError()