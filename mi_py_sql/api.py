# built-in
from typing import Any, Union
import inspect, os
from concurrent.futures import ThreadPoolExecutor
# pip
import aiosqlite
# local
from mi_py_sql.utils.exec import exec
# public vars

# use this class to init the api
class init:
    def __init__(self, sqlite_path=":memory:"):
        self._sqlite_path = sqlite_path
    
    async def __aenter__(self):
        await shutdown()
        global _sqlite_path
        _sqlite_path = self._sqlite_path
        return self

    async def __aexit__(self, *excinfo):
        await shutdown()
        
# public functions
async def table_add_col( id:str, col_id:str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def table_remove_col( id:str, col_id:str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def table_set( id:str, name:str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def table_get( id:str ) -> Union[None, dict]:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def table_del( id:str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )


async def column_set( id:str, name:str, type:str, primary_key:bool=False, unique:bool=False, default_value=None ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def column_get( id:str ) -> Union[None, dict]:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def column_del( id:str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )


async def conf_assert_table():
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def conf_get( key: str, default:Any=None ) -> Union[Any, None]:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )
    
async def conf_set( key: str, value: Any ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )

async def conf_del( key: str ) -> bool:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), True )

async def hello( name: str ) -> None:
    return await _exec( inspect.currentframe().f_code.co_name, locals(), False )

async def run_from_command_line( funcs:list[callable] ):
    return await _exec( inspect.currentframe().f_code.co_name, locals(), False )

async def shutdown() -> None:
    global _db
    if _db != None:
        await _db.close()
        _db = None
                           
# protected symbols
async def _exec( function_name:str, args:dict, add_db:bool=True ) -> Any:      
    if add_db:      
        global _db
        if _db is None:
            _db = await aiosqlite.connect(_sqlite_path)      
        args["db"] = _db            
    return await exec( function_name, args, _api_functions_dir )   

_sqlite_path=":memory:"
_db:aiosqlite.Connection=None
_api_functions_dir = os.path.realpath( os.path.dirname(__file__) + "/api_functions" )