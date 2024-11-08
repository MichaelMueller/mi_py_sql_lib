# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def conf_del( db:aiosqlite.Connection, key: str ) -> bool:
    await mi_py_sql.api.conf_assert_table()
    affected_rows = 0
    async with db.execute("DELETE FROM config WHERE key = ?", ( key, ) ) as cursor:
        affected_rows = cursor.rowcount
    await db.commit()
    return affected_rows == 1