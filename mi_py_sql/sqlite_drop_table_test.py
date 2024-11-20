
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip
import aiosqlite, sqlite3

from mi_py_essentials import AbstractTest, Test
from mi_py_sql import SqliteDatabase
from mi_py_sql.sqlite_rename_table_test import SqliteRenameTableTest

class SqliteDropTableTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        
    def dependent_tests(self) -> list[Test]:
        return [ SqliteRenameTableTest() ]
    
    async def _exec(self) -> None:
        tmp_dir = await self.tmp_dir()
        db_path = f'{tmp_dir}/test_db.sqlite3'
        db = SqliteDatabase( db_path )        
        await db.create_table("users").int_auto_increment_pk( "id" ).exec()              
        await db.drop_table("users").exec()        
        await db.drop_table("users").if_exists().exec()      
                  
        rename_table = db.rename_table("users").to("new_users")  
        await self._expect_async_exception(rename_table.exec, "calling rename_table.exec on a dropped table", sqlite3.OperationalError)