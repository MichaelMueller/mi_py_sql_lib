from typing import Any, Iterable, TYPE_CHECKING

# local
if TYPE_CHECKING:
    from mi_py_sql.sqlite_database import SqliteDatabase    
from mi_py_sql.rename_table import RenameTable

class SqliteRenameTable(RenameTable):
    """SQLite-specific implementation of CreateTable."""

    def __init__(self, database:"SqliteDatabase", table_name:str) -> None:
        super().__init__(database, table_name)
    
    def database(self) -> "SqliteDatabase":
        return super().database()
    
    async def exec(self) -> "SqliteDatabase":
        """
        Execute the generated SQL query using the database connection.
        """
        query = self.to_sql([])
        await self.database().execute_write( query )
        return self.database()

    def to_sql(self, _: Iterable[Any]) -> str:
        return f'ALTER TABLE {self.name()} RENAME TO {self._new_name};'