# local
from .interfaces.DBMS import DBMS

class SQLiteDBMS(DBMS):    
    def __init__(self) -> None:        
        super().__init__()