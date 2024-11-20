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
        self._values = list(values)
        return self
        
    def to_sql( self ) -> Tuple[str, Iterable[Any]]:
        placeholders = ["?"] * len(self._values)
        
        sql =  'INSERT INTO '+self.name()+' ('
        sql += ', '.join(self._columns)
        sql += ') VALUES ('
        sql +=  ', '.join(placeholders) + ');'
        
        return sql, self._values
        