import aiosqlite

async def conf_assert_table( db:aiosqlite.Connection ):
    await db.execute("""
            CREATE TABLE IF NOT EXISTS config (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
    await db.commit()