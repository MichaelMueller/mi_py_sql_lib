
from typing import Coroutine, Union, Any, Optional
import json, os, tempfile, asyncio, shutil, logging
# pip
import aiosqlite, sqlite3

from mi_py_essentials import AbstractTest, Test
from mi_py_sql import SqliteDatabase, SqliteCreateTable
from mi_py_sql.sqlite_database_test import SqliteDatabaseTest

class SqliteCreateTableTest(AbstractTest):
    def __init__(self) -> None:
        super().__init__()
        
    def dependent_tests(self) -> list[Test]:
        return [ SqliteDatabaseTest() ]
    
    async def _exec(self) -> None:
        tmp_dir = await self.tmp_dir()
        db_path = f'{tmp_dir}/test_db.sqlite3'
        db = SqliteDatabase( db_path )
        
        create_table = db.create_table("users") \
            .int_auto_increment_pk( "id" ) \
            .string( "name", 256 ).unique() \
            .float( "age" ).default_value(25.0) \
            .blob("image", 65000)
        
        target_sql = "CREATE TABLE users (id INTEGER AUTO INCREMENT PRIMARY KEY, name TEXT UNIQUE, age REAL DEFAULT 25.0, image BLOB);".lower().replace(" ", "")
        sql, _ = create_table.to_sql()
        self._print( sql )
        
        self._assert( sql.lower().replace(" ", "").startswith( target_sql ), "test table users could be created" )
        await create_table.exec()
                
        await self._expect_async_exception(create_table.exec, "calling create_table.exec twice", sqlite3.OperationalError)
        
        await create_table.if_not_exists().exec() # shall not raise an exception
        