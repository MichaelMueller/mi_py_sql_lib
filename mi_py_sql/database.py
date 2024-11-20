# forward declerations
from typing import TYPE_CHECKING
    
# other imports
if TYPE_CHECKING:
    from mi_py_sql import CreateTable
    from mi_py_sql import RenameTable

class Database:    
    
    def name(self) -> str:
        raise NotImplementedError()     
     
    def create_table(self, name:str) -> "CreateTable":
        raise NotImplementedError()    
    
    def rename_table(self, name:str) -> "RenameTable":
        raise NotImplementedError()    
    
    