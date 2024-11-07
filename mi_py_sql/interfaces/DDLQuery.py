from typing import Tuple, Any, Iterable, TYPE_CHECKING
from .SqlQuery import SqlQuery
if TYPE_CHECKING:
    from .Schema import Schema

class DDLQuery(SqlQuery):
  
    def schema(self) -> "Schema":
        raise NotImplementedError()