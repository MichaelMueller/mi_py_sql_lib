# built-in
import tempfile

# pip
from mi_py_test.Test import Test
from mi_py_test.AbstractTest import AbstractTest

# local
# interfaces
from ..interfaces.DBMS import DBMS
from ..interfaces.Table import Table
# interface tests
from .DBMSTest import DBMSTest
# implementations
from ..sqlite.SQLiteDBMS import SQLiteDBMS

class MiPySqlTestSuite(AbstractTest):    
    def __init__(self) -> None:        
        super().__init__()        
        self._test_db_name = "6c4ad2db-cb84-40d7-abf7-a3aafab11e82" # for the name a uuid is used to not collide with other databases        
        self._instance:DBMS = None
        
    def dependent_tests(self) -> list[Test]:
        self._instance = SQLiteDBMS( tempfile.mkdtemp() )
        
        return [ DBMSTest( self._instance ) ]
    
    async def _exec(self):       
        # testing sqlite.exec()
        pass