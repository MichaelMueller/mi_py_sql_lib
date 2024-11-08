from typing import Tuple, Any, Iterable, TypedDict

class Query:
    
    async def exec(self) -> Any:
        raise NotImplementedError()    
    
    def to_sql(self) -> Tuple[str, Iterable[Any]]:
        raise NotImplementedError()
    