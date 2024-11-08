from mi_py_sql.Serializable import Serializable
from mi_py_sql.Library import Library

class AbstractFunction:    
    
    def __init__(self, library:Library, file_path:str) -> None:
        self._library = library
        self._file_path = file_path
        
    async def exec( self, _ : Serializable ) -> Serializable:
        raise NotImplementedError()