# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql import Database
from mi_py_sql import Query

class RenameTable(Query):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database", name:str) -> None:
        super().__init__()
        self._database = database
        self._name = name
        self._new_name = None
        
    def database(self) -> "Database":
        return self._database                     
    
    def to(self, name:str ) -> "RenameTable":
        self._new_name = name
        return self
    
    def new_name(self, name:str ) -> "RenameTable":
        self._new_name = name
        return self