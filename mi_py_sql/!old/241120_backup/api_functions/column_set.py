# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def column_set( db:aiosqlite.Connection, id:str, name:str, type:str, primary_key:bool=False, unique:bool=False, default_value=None ) -> None:
    props = locals().copy()
    del props["db"]
    del props["id"]
    
    # create or update the column
    columns = await mi_py_sql.api.conf_get("columns", {})
    column = columns[id] if id in columns else {}
    column.update( props )
    columns[id] = props
    
    return await mi_py_sql.api.conf_set("columns", columns)