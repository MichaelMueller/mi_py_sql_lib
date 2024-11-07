# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Database import Database
    
# other imports
from .Table import Table
from .CreateTableQuery import CreateTableQuery

class Schema:
    
    # parent
    def database(self) -> "Database": 
        raise NotImplementedError()             
    
    # queries    
    def create_table_query(self, table_name:str) -> CreateTableQuery: 
        raise NotImplementedError()             
    
    # getter
    def table_names(self) -> list[str]:
        raise NotImplementedError()
    
    def table_exists(self, table_name:str) -> bool:
        raise NotImplementedError()
        
    def tables(self) -> list[Table]:
        raise NotImplementedError()