from typing import Any, Iterable, TYPE_CHECKING

# local
if TYPE_CHECKING:
    from mi_py_sql.sqlite_database import SqliteDatabase    
from mi_py_sql.drop_table import DropTable

class SqliteDropTable(DropTable):
    """SQLite-specific implementation of CreateTable."""

    def __init__(self, database:"SqliteDatabase", table_name:str) -> None:
        super().__init__(database, table_name)
    
    def database(self) -> "SqliteDatabase":
        return super().database()
    
    async def exec( self, args:Iterable[Any]=[] ) -> "SqliteDatabase":
        await super().exec( args )
        return self.database()

    def to_sql(self) -> str:
        return f'DROP TABLE{" IF EXISTS" if self._if_exists else ""} {self.name()};'