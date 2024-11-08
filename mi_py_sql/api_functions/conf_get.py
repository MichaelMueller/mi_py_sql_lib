# built-in
from typing import Any, Union
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def conf_get( db:aiosqlite.Connection, key: str, default:Any=None ) -> Union[Any, None]:
    await mi_py_sql.api.conf_assert_table()
    
    cursor = await db.execute("SELECT value FROM config WHERE key = ?", (key,))
    row = await cursor.fetchone()
    return json.loads( row[0] ) if row else default