from typing import Tuple, Any, Iterable, TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from mi_py_sql import Database

class Query:
    
    def database(self) -> "Database":
        raise NotImplementedError()    
        
    async def exec( self ) -> Any:
        raise NotImplementedError()    
    
    def to_sql( self, args:Iterable[Any] ) -> str:
        raise NotImplementedError()
    