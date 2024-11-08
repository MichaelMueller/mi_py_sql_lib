# built-in
from typing import Any, Optional, Iterable, Union
import importlib, os, aiofiles.os
import asyncio
import importlib.util
import logging
from concurrent.futures import ThreadPoolExecutor
# pip
import aiosqlite
# local
from .Query import Query

Serializable = Union[int, float, str, bool, None, list, dict[str, "Serializable"]]

class Library:    
    
    def __init__(self, sqlite_address=":memory:") -> None:
        self._sqlite_address = sqlite_address
        self._db:aiosqlite.Connection = None
        self._functions_dir = os.path.dirname(__file__) + "/functions"
            
    async def exec( self, function_name:str, args:Union[None,dict] ) -> Union[int, float, str, bool, None, list, dict]:
        class_ = None
        module_path = self._functions_dir + "/" + function_name + ".py"
        if await aiofiles.os.path.exists(module_path):
            module = await self._load_module_from_path_async(module_path, function_name)
            class_ = getattr(module, function_name)
            await class_( self, module_path )
        assert class_ != None, f'Function "{function_name}" not found in {query_processor_dirs}'                       
        return await func_() if args == None else func_( **args )                   
    
    async def db(self) -> None:        
        if self._db is None:
            db_path = self._sqlite_address 
            self._db = await aiosqlite.connect( db_path )                    

    async def close(self) -> None:
        if self._db != None:
            await self._db.close()
            self._db = None   
            
    def _load_module_from_path_sync(self, module_path, module_name):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)        
        spec.loader.exec_module(module)                
            
        return module

    async def _load_module_from_path_async(self, module_path, module_name):
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            # Run the blocking load function in the executor and await its result
            module = await loop.run_in_executor(pool, self._load_module_from_path_sync, module_path, module_name)
                
            setattr("db", self._db)    
            
            return module