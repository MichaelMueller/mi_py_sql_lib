# forward declerations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Table import Table

class Column:
    
    def table(self) -> "Table":
        pass