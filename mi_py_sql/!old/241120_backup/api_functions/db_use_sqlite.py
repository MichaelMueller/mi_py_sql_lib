# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def connect_to_sqlite( db:aiosqlite.Connection, sqlite_path ) -> None:
    
    
    return await mi_py_sql.api.conf_set("db_configs", db_configs)