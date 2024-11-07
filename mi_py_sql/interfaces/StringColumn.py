# forward declerations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    from .Table import Table
from .Column import Column

class StringColumn(Column):
    
    def max_length(self) -> int:
        raise NotImplementedError()
    
    def default_value(self) -> Union[None, str]:
        raise NotImplementedError()