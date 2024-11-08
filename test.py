import asyncio
from mi_py_sql.MiPySql import MiPySql
from mi_py_sql.Query import Query

async def test():
    mipysql = MiPySql()
    q:Query = {"name": "hello_world"}
    await mipysql.exec( q )

if __name__ == "__main__":
    asyncio.run(test())
