from typing import Tuple, Any, Iterable
from .Query import Query
class SqlQuery(Query):
  
    def to_sql(self) -> Tuple[str, Iterable[Any]]:
        raise NotImplementedError()