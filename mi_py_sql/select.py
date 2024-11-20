# built-in imports
from typing import Any, List, Optional, TYPE_CHECKING, Iterable
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql.database import Database
from mi_py_sql.query import Query

class Select(Query):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database") -> None:
        super().__init__(database)     
        