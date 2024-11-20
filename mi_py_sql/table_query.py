# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING, Iterable
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql import Database
from mi_py_sql import Query

class TableQuery(Query):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database", table_name:str) -> None:
        super().__init__(database)
        self._name = table_name
        
    def name(self) -> str:
        return self._name                   
        