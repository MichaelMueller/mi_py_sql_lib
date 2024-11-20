# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING, Iterable
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql.database import Database

from mi_py_sql.table_query import TableQuery

class DropTable(TableQuery):
    """ fluent interface for dropping a table """
    
    def __init__(self, database:"Database", name:str) -> None:
        super().__init__(database, name)        
        self._if_exists = None        

    def if_exists( self, if_exists:bool=True ) -> "DropTable":       
        self._if_exists = if_exists
        return self