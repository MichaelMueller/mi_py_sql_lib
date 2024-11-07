# built-in imports
from typing import Any

# local imports
from .Query import Query

class CreateTableQuery(Query): 
    
    def set_name(name:str) -> "CreateTableQuery":
        raise NotImplementedError()
    
    def int_col(self, name:str) -> "CreateTableQuery":
        raise NotImplementedError()
    
    def float_col(self, name:str) -> "CreateTableQuery":
        raise NotImplementedError()
    
    def string_col(self, name:str, max_len:int) -> "CreateTableQuery":
        raise NotImplementedError()
    
    