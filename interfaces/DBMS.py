from .Database import Database

class DBMS:
    
    async def database_names(self) -> list[str]:
        raise NotImplementedError()
    
    async def database_exists(self, name:str) -> bool:
        raise NotImplementedError()
    
    async def database(self, name:str) -> Database:
        raise NotImplementedError()
    
    async def drop_database(self, database_name) -> "DBMS":
        raise NotImplementedError()