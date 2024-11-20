# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING, Iterable
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql import Database
    from mi_py_sql.database import Database
from mi_py_sql import TableQuery

class RenameTable(TableQuery):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database", name:str) -> None:
        super().__init__(database, name)     
        
        self._new_name:str = None   
        
    def to( self, new_name:str ) -> "RenameTable":       
        self._new_name = new_name
        return self