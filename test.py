from typing import Any
import asyncio, os, logging, json
import aiosqlite

import mi_py_sql.api
   
async def main() -> Any:
    sqlite_path = os.getenv("mi_py_sql_api_sqlite_path", mi_py_sql.api.sqlite_path)     
    async with mi_py_sql.api.init(sqlite_path):      
        callable_functions = [ 
            mi_py_sql.api.hello,        
            mi_py_sql.api.conf_assert_table,        
            mi_py_sql.api.conf_set,        
            mi_py_sql.api.conf_get,        
            mi_py_sql.api.conf_del,        
            mi_py_sql.api.column_set,        
            mi_py_sql.api.column_get,        
            mi_py_sql.api.column_del,        
            mi_py_sql.api.table_add_col,        
            mi_py_sql.api.table_remove_col,        
            mi_py_sql.api.table_set,        
            mi_py_sql.api.table_get,        
            mi_py_sql.api.table_del
        ]
        result = await mi_py_sql.api.run_from_command_line( callable_functions )
        print(json.dumps( result ) )
   
if __name__ == "__main__":
    result = asyncio.run( main() )
          