# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def table_set( db:aiosqlite.Connection, id:str, name:str ) -> bool:
    props = locals().copy()
    del props["db"]
    del props["id"]
    props["columns"] = []
    
    # create or update the table
    tables = await mi_py_sql.api.conf_get("tables", {})
    table = tables[id] if id in tables else {}
    table.update( props )
    tables[id] = props
    
    return await mi_py_sql.api.conf_set("tables", tables)