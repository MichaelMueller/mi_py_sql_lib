# forward declerations
from typing import Union    
from .IntColumn import IntColumn

class IntPrimaryKeyColumn(IntColumn):
        
    def is_auto_incremented(self) -> bool:
        raise NotImplementedError()