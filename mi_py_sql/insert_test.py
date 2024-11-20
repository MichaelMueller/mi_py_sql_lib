
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip
import aiosqlite, sqlite3

from mi_py_essentials import AbstractTest, Test
from mi_py_sql import SqliteDatabase
from mi_py_sql.sqlite_drop_table_test import SqliteDropTableTest

class InsertTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        
    def dependent_tests(self) -> list[Test]:
        return [ SqliteDropTableTest() ]
    
    async def _exec(self) -> None:
        tmp_dir = await self.tmp_dir()
        db_path = f'{tmp_dir}/test_db.sqlite3'
        db = SqliteDatabase( db_path )
        
        create_table = db.create_table("users") \
            .int_auto_increment_pk( "id" ) \
            .string( "name", 256 ).unique()
        await create_table.exec()
        await db.insert_into("users").columns("name").values("mueller").exec()