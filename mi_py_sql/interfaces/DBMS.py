from .Database import Database

class DBMS:
    
    async def database_names(self) -> list[str]:
        raise NotImplementedError()
        
    async def drop_database(self, database_name:str) -> bool:
        raise NotImplementedError()
    
    async def create_database(self, database_name:str) -> Database: 
        raise NotImplementedError()  
    
    async def database_exists(self, name:str) -> bool:
        raise NotImplementedError()
    
    async def database(self, name:str) -> Database:
        raise NotImplementedError()