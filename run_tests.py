# built-in
import asyncio, sys

# local
from mi_py_sql.tests.MiPySqlTestSuite import MiPySqlTestSuite

async def main() -> bool:        
    return await MiPySqlTestSuite().exec()    
        
if __name__ == "__main__":
    tests_ok = asyncio.run(main())
    sys.exit( 0 if tests_ok else 1 )