# built-in
from typing import Any
import importlib, importlib.util, asyncio
from concurrent.futures import ThreadPoolExecutor

# pip
import aiosqlite
           
async def load_module_from_path_async(module_path, module_name) -> None:    
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        # Run the blocking load function in the executor and await its result
        module = await loop.run_in_executor(pool, _load_module_from_path_sync, module_path, module_name)
        return module
    
def _load_module_from_path_sync(module_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)        
    spec.loader.exec_module(module)                
        
    return module