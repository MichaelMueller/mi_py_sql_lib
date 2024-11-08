# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def table_add_col( db:aiosqlite.Connection, id:str, col_id:str ) -> None:
    tables = await mi_py_sql.api.conf_get("tables", {})  
    if not col_id in tables[id]["columns"]:      
        tables[id]["columns"].append( col_id )    
        return await mi_py_sql.api.conf_set("tables", tables)
    return False