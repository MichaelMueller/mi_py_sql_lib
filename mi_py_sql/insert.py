# built-in imports
from typing import Any, List, TYPE_CHECKING, Iterable, Tuple
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
        self._values:List[Any] = None   
        
    def columns( self, *columns:str ) -> "Insert":  
        self._columns = list(columns)
        return self
    
    def values( self, *values:Any ) -> "Insert":  
        self._columns = list(values)
        return self
        
    def to_sql( self ) -> Tuple[str, Iterable[Any]]:
        sql =  'INSERT INTO table_name ('
        sql += ', ".join(self._columns)'
        sql += ') VALUES ('
        sql += ["?"] * len(self._values) + ';'
        return sql, self._values
        