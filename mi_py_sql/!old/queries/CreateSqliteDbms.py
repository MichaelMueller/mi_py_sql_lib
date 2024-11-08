from typing import Literal, Annotated, Optional
from mi_py_sql.Query import Query

class CreateSqliteDbms(Query):
    name            : Literal  ["create_sqlite_dbms"]
    working_dir     : Annotated[ Optional[str], { "help": "If not set a temp dir will be used" } ]
    default_ext     : Annotated[ Optional[str], {" default_value": ".sqlite3" } ]
    