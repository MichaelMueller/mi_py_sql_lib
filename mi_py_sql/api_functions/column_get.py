# built-in
from typing import Union, Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def column_get( db:aiosqlite.Connection, id:str ) -> None:
    columns = await mi_py_sql.api.conf_get("columns", {})
    return columns[id] if id in columns else None