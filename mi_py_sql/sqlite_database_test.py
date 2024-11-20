
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip
import aiosqlite

from mi_py_essentials import AbstractTest
from mi_py_sql.sqlite_database import SqliteDatabase

class SqliteDatabaseTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        self._temp_dir = None
        
    async def _exec(self) -> None:
        tmp_dir = await self.tmp_dir()
        db_path = f'{tmp_dir}/test_db.sqlite3'
        db = SqliteDatabase( db_path )
        
        self._assert( db.path() == db_path, f'db.path() test' )
        
        lib_name_key = "lib_name"
        lib_name = "mi_py_sql"
        await db.execute_write("CREATE TABLE test_config (name TEXT PRIMARY KEY, value TEXT)", [])
        await db.execute_write("INSERT INTO test_config (name, value) VALUES (?, ?)", (lib_name_key, lib_name))
        
        res = await db.execute( "select value FROM test_config WHERE name = ?", (lib_name_key,) )
        queried_lib_name = res[0][0]

        self._assert( queried_lib_name == lib_name, f'expected queried_lib_name == "{lib_name}", got "{queried_lib_name}"')

    