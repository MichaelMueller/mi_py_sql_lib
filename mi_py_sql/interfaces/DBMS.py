from .Database import Database
from .CreateDatabaseQuery import CreateDatabaseQuery
from .DropDatabaseQuery import DropDatabaseQuery
from .Database import Database

class DBMS:
    
    # queries   
    def drop_database_query(self, database_name:str) -> DropDatabaseQuery:
        raise NotImplementedError()
    
    def create_database_query(self, database_name:str) -> CreateDatabaseQuery: 
        raise NotImplementedError()  
    
    # getter
    async def database_names(self) -> list[str]:
        raise NotImplementedError()
    
    async def database_exists(self, name:str) -> bool:
        raise NotImplementedError()
    
    async def database(self, name:str) -> Database:
        raise NotImplementedError()
    
    # other
    async def disconnect(self) -> None:
        raise NotImplementedError()