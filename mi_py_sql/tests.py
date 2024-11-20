import sys, asyncio, os, logging
from typing import Callable, Dict, Any, Optional, List, get_origin, get_args
# pip
from mi_py_essentials import Test, AbstractTest
# local
from mi_py_sql import SqliteDatabaseTest

class Tests(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
                
    async def exec(self) -> bool:   
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[ logging.StreamHandler() ] )
        tests_passed = await super().exec() 
        sys.exit( 0 if tests_passed else 1 )
        
    def dependent_tests(self) -> list[Test]:
        return [ SqliteDatabaseTest() ]
    
    async def _exec(self) -> None:
        pass

if __name__ == "__main__":
    asyncio.run( Tests().exec() )