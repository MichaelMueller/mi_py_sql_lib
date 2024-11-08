from typing import TypedDict, Optional, Any
from .Query import Query

class DeleteDbms(TypedDict):    
    name:str
    result:Optional[Any]