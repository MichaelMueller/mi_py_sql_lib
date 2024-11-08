from typing import Any
import asyncio, os, logging, json
import aiosqlite
import inspect

import mi_py_sql.api
   
class test:
    
    def foo(self):
        print("foo")
        # Get the signature of the function
        
t = test()
signature = inspect.signature(test.foo)
signature = inspect.signature(t.foo)

# Print the signature
print(signature)  # Output: (a: int, b: str = 'hello', *args, **kwargs)
        
          