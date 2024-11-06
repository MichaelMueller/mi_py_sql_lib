# built-in
import asyncio
import argparse
import tempfile
import os

# local
from mi_py_sql.tests.DBMSTest import DBMSTest
from mi_py_sql.sqlite.SQLiteDBMS import SQLiteDBMS

async def main():    
    
    await DBMSTest( SQLiteDBMS( tempfile.mkdtemp() ) ).exec()    
        
if __name__ == "__main__":
    asyncio.run(main())