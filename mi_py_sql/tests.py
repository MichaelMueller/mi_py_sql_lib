import sys, asyncio, os, logging
from typing import Callable, Dict, Any, Optional, List, get_origin, get_args
# pip
from mi_py_essentials import Test, AbstractTest
# local
from mi_py_sql.insert_test import InsertTest

class Tests(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[ logging.StreamHandler() ] )
                
    def dependent_tests(self) -> list[Test]:
        return [ InsertTest() ]
    
    async def _exec(self) -> None:
        pass

if __name__ == "__main__":
    tests_passed = asyncio.run( Tests().exec() )
    sys.exit( 0 if tests_passed else 1 )