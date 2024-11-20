# built-in imports
from typing import Any, List, Optional, TYPE_CHECKING, Iterable
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql.database import Database
from mi_py_sql import TableQuery

class Insert(TableQuery):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database", name:str) -> None:
        super().__init__(database, name)     
        
        self._columns:List[str] = None   
        self._values:List[str] = None   
        
    def columns( self, *columns:str ) -> "Insert":  
        self._columns = list(columns)
        return self
    
    def values( self, *values:Any ) -> "Insert":  
        self._columns = list(values)
        return self