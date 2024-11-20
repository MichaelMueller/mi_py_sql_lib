
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip

from mi_py_essentials import AbstractTest

class SqliteDatabaseTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        self._temp_dir = None
        
    async def _exec(self) -> None:
        self._print("Runn!!!!!")
        
    
    