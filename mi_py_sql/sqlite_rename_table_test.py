
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip
import aiosqlite, sqlite3

from mi_py_essentials import AbstractTest, Test
from mi_py_sql import SqliteDatabase
from mi_py_sql.sqlite_create_table_test import SqliteCreateTableTest

class SqliteRenameTableTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        
    def dependent_tests(self) -> list[Test]:
        return [ SqliteCreateTableTest() ]
    
    async def _exec(self) -> None:
        tmp_dir = await self.tmp_dir()
        db_path = f'{tmp_dir}/test_db.sqlite3'
        db = SqliteDatabase( db_path )
        
        create_table = db.create_table("users") \
            .int_auto_increment_pk( "id" ) \
            .string( "name", 256 ).unique() \
            .float( "age" ).default_value(25.0) \
            .blob("image", 65000)
                
        await create_table.exec()
        await db.rename_table("users").to("new_users").exec()
                
        create_table = db.create_table("new_users") \
            .int_auto_increment_pk( "id" )
            
        await self._expect_async_exception(create_table.exec, "calling create_table.exec another time with the new name", sqlite3.OperationalError)