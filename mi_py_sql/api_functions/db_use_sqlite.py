# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def connect_to_sqlite( db:aiosqlite.Connection, sqlite_path ) -> None:
    props = locals().copy()
    del props["db"]
    del props["id"]
    
    # create or update the db_config
    db_configs = await mi_py_sql.api.conf_get("db_configs", {})
    db_config = db_configs[id] if id in db_configs else {}
    db_config.update( props )
    db_configs[id] = props
    
    return await mi_py_sql.api.conf_set("db_configs", db_configs)