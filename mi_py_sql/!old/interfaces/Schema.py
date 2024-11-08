# forward declerations
from typing import TypedDict, Dict, Union
        
class Column(TypedDict):
    type_:Union[str, int, float, bytes]
    is_primary_key:bool
    is_unique:bool
    is_nullable:bool
    is_auto_increment:bool
    max_length:Union[None, int]
    default_value:Union[int, float, str, bytes, None]
    referenced_column:Union[None, "Column"]
    
class Table(TypedDict):
    columns:Dict[str, Column]
    
class Schema(TypedDict):
    tables:Dict[str, Table]