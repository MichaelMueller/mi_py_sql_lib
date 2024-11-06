from mi_py_sql_lib.libs.mi_py_test_lib.AbstractTest import AbstractTest
from mi_py_sql_lib.interfaces.DBMS import DBMS

class DBMSTest (AbstractTest):
    
    def __init__(self, instance:DBMS) -> None:        
        super().__init__()
        
        self._instance = instance
        
    async def _exec(self):
        # delete previous databases
        for name in await self._instance.database_names():
            self._instance.drop_database( name )
        self._assert( len(self._instance.database_names()) == 0, "all databases have been dropped at test start" )
        
        # create user database