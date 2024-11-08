import importlib, os, aiofiles.os
import asyncio
import importlib.util
import sys
from concurrent.futures import ThreadPoolExecutor
from .Query import Query

class MiPySql:    
    
    def __init__(self, query_processor_dirs=[]) -> None:
        self._query_processor_dirs = [ dir_ for dir_ in query_processor_dirs ]
        # add default processor dir
        default_query_processors_dir = os.path.dirname(__file__) + "/default_query_processors" 
        if default_query_processors_dir not in self._query_processor_dirs:
            self._query_processor_dirs.append( default_query_processors_dir )    
        
    async def exec( self, q:Query ) -> None:
        query_name = q["name"]        
        func_ = None
        
        # search in all paths for the processor
        for query_processor_dir in self._query_processor_dirs:
            module_file_path = query_processor_dir + "/" + query_name + ".py"
            if await aiofiles.os.path.exists(module_file_path):
                module = await self._load_module_from_path_async(module_file_path, query_name)
                func_ = getattr(module, query_name)
                break
        
        assert func_ != None, f'Query processor for "{query_name}" not in {self._query_processor_dirs}'
        func_( q )
        
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
            return module