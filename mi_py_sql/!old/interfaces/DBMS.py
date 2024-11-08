from typing import Optional, Union
from .Database import Database
from .Database import Database

class DBMS:
            
    # database managment
    async def database(self, database_name:str, create:Optional[bool]=False) -> Union[None, Database]: 
        """ 
        will try to load and select to the database indicated by "database_name"
        if it not exists None will be created if "create" is False, otherwise an empty database will be created
        """
        raise NotImplementedError()
    
    async def database_names(self) -> list[str]:
        """ will load all existing database names """
        raise NotImplementedError()
        
    async def drop_database(self, database_name:str) -> "DBMS": 
        """ 
        closes the database if it was opened, then drops it completely
        will do nothing if the database does not exist
        """
        raise NotImplementedError()  
    
    async def close_all(self) -> None: 
        """ will try to load and select to the database, returns none if not exists """
        raise NotImplementedError()