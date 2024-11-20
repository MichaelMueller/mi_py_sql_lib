# built-in
from typing import Union, Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def table_get( db:aiosqlite.Connection, id:str ) -> Union[None, dict]:
    tables = await mi_py_sql.api.conf_get("tables", {})
    return tables[id] if id in tables else None