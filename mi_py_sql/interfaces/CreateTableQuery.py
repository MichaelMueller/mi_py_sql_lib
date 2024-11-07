# built-in imports
from typing import Any, Union, Optional

# local imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Schema import Schema
    
from .SqlQuery import SqlQuery
from .Column import Column

class CreateTableQuery(SqlQuery):
     
    async def exec(self) -> None:
        raise NotImplementedError()
    
    def schema(self) -> "Schema":
        raise NotImplementedError()
        
    def int_col(self, 
                name:str, 
                default_value:Optional[int]=None, 
                primary_key:bool=False, 
                unique:Optional[bool]=False, 
                nullable:Optional[bool]=False, 
                referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        raise NotImplementedError()
    
    def float_col(self, 
                  name:str, 
                  default_value:Union[float, None]=None, 
                  primary_key:bool=False, 
                  unique:Optional[bool]=False, 
                  nullable:Optional[bool]=False, 
                  referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        raise NotImplementedError()
        
    def string_col(self, 
                   name:str, 
                   max_length:int, 
                   default_value:Union[str, None]=None, 
                   primary_key:bool=False, 
                   unique:Optional[bool]=False, 
                   nullable:Optional[bool]=False, 
                   referenced_col:Optional[Column]=None) -> "CreateTableQuery":
        
        raise NotImplementedError()
        
    def int_primary_key_col(self, 
                            name:str, 
                            auto_increment:Optional[bool]=True) -> "CreateTableQuery":
        raise NotImplementedError()
    
    def if_not_exists( self, if_not_exists:bool=True ) -> "CreateTableQuery":
        raise NotImplementedError()