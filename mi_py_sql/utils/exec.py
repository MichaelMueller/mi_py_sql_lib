# built-in
from typing import Any
import os
# pip
import aiosqlite     
# local
from mi_py_sql.utils.load_module_from_path_async import load_module_from_path_async
   
async def exec( function_name:str, args:dict, dir:str ) -> Any:   
    module_path = dir + "/" + function_name + ".py"
    module = await load_module_from_path_async(module_path, function_name)
    func_ = getattr(module, function_name)     
    return await func_(**args) if len(args) > 0 else await func_()       