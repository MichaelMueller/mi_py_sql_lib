# built-in
# pip
import aiosqlite
# local
import mi_py_sql.api

async def column_del( db:aiosqlite.Connection, id:str ) -> None:
    columns = await mi_py_sql.api.conf_get("columns", {})
    if id in columns:
        del columns[id]
        return await mi_py_sql.api.conf_set("columns", columns)
    