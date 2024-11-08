# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def table_remove_col( db:aiosqlite.Connection, id:str, col_id:str ) -> bool:
    tables = await mi_py_sql.api.conf_get("tables", {})  
    l:list = tables[id]["columns"]
    if col_id in l:
        l.remove( col_id )
        return await mi_py_sql.api.conf_set("tables", tables)
    return False