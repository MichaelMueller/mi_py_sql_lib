# forward declerations
from typing import TYPE_CHECKING, Any, Iterable
    
# other imports
if TYPE_CHECKING:
    from mi_py_sql.query import Query
    from mi_py_sql.create_table import CreateTable
    from mi_py_sql.rename_table import RenameTable
    from mi_py_sql.drop_table import DropTable

class Database:    
    
    def name(self) -> str:
        raise NotImplementedError()     
     
    def create_table(self, name:str) -> "CreateTable":
        raise NotImplementedError()    
    
    def rename_table(self, name:str) -> "RenameTable":
        raise NotImplementedError()    
    
    def drop_table(self, name:str) -> "DropTable":
        raise NotImplementedError()    
    
    async def exec( self, q:"Query" ) -> Any:
        raise NotImplementedError()    