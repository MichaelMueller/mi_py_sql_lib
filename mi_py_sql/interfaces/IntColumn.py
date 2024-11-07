# forward declerations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    from .Table import Table
from .Column import Column

class IntColumn(Column):
    
    def max_length(self) -> int:
        raise NotImplementedError()
    
    def default_value(self) -> Union[None, int]:
        raise NotImplementedError()