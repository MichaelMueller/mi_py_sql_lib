# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Database import Database
    
# other imports
from .Table import Table
from .Column import Column

class Schema:
    
    def database(self) -> "Database":
        pass
    
    async def table_names(self) -> list[str]:
        raise NotImplementedError()
        
    async def drop_table(self, table_name:str) -> bool:
        raise NotImplementedError()
    
    def create_table(self, name:str, columns:list[Column], primary_keys:list[str], unique_keys:list[str]=[]) -> "Table":
        raise NotImplementedError()
    
    async def table_exists(self, name:str) -> bool:
        raise NotImplementedError()
    
    async def table(self, name:str) -> Table:
        raise NotImplementedError()
    
    async def tables(self) -> list[Table]:
        raise NotImplementedError()
        
    def create_integer_column( self, name:str ) -> "Column":
        raise NotImplementedError()
    
    def create_string_column( self, name:str, max_length:int ) -> "Column":
        raise NotImplementedError()