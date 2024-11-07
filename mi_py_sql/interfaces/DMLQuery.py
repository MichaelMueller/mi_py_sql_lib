from typing import TYPE_CHECKING
from .SqlQuery import SqlQuery
if TYPE_CHECKING:
    from .Database import Database

class DMLQuery(SqlQuery):
  
    def database(self) -> "Database":
        raise NotImplementedError()