from ..interfaces2.Dbms import Dbms
from ..interfaces2.DbmsQuery import DbmsQuery
from ..interfaces2.DbExists import DbExists
from ..interfaces2.CreateDb import CreateDb

class SqliteDbms(Dbms):
    
    def __init__(self, databases_directory:str, sqlite_ext:str=".sqlite3") -> None:        
        super().__init__()
        self._databases_directory = databases_directory
        self._sqlite_ext = sqlite_ext
      
    async def exec( self, query:DbmsQuery ) -> None:
        func_name = f'_{query["name"]}'
        func_ = getattr(self, func_name)
        func_(query)
    
    async def _create_db( self, query:CreateDb ) -> None:
        pass
    
    async def _select_db( self, query:DbExists ) -> None:
        pass