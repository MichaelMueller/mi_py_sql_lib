# built-in
import asyncio
import argparse

# local
from mi_py_sql.tests.DBMSTest import DBMSTest
from mi_py_sql.SQLiteDBMS import SQLiteDBMS

async def main():
    await DBMSTest( SQLiteDBMS() ).exec()    
        
if __name__ == "__main__":
    asyncio.run(main())