# built-in
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def table_del( db:aiosqlite.Connection, id:str ) -> bool:
    tables = await mi_py_sql.api.conf_get("tables", {})
    if id in tables:
        del tables[id]
        return await mi_py_sql.api.conf_set("tables", tables)
    return False