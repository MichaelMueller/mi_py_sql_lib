# built-in
from typing import Any
import json
# pip
import aiosqlite
# local
import mi_py_sql.api

async def conf_set( db:aiosqlite.Connection, key: str, value: Any ) -> bool:
    await mi_py_sql.api.conf_assert_table()
    await db.execute("""
        INSERT INTO config (key, value) 
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value = excluded.value
    """, (key, json.dumps( value, indent=2 ) ) )
    await db.commit()
    return True