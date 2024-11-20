import aiosqlite
import asyncio
import sqlite3


connection = None
async def run_query_unsafe(query, params=()):
    global connection
    connection = await aiosqlite.connect(":memory:")
    await connection.execute(query, params)
    await connection.commit()
    print("Query executed successfully")
        
async def run_query(db_path, query, params=()):
    try:
        async with aiosqlite.connect(db_path) as db:
            await db.execute(query, params)
            await db.commit()
            print("Query executed successfully")
    except sqlite3.OperationalError as e:
        print(f"OperationalError occurred: {e}")
        # Optional: Log the error, retry, or take other actions

async def main():

    # Simulate an intentional error for demonstration
    faulty_query = "INSERT INTO non_existing_table (value) VALUES (?)"
    
    # Handle the error gracefully
    await run_query_unsafe( faulty_query, ("test",))

asyncio.run(main())