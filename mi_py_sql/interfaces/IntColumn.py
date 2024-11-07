# forward declerations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    from .Table import Table
from .Column import Column

class IntColumn(Column):
        
    def default_value(self) -> Union[None, int]:
        raise NotImplementedError()