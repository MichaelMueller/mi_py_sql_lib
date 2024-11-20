from typing import Any, Iterable, TYPE_CHECKING, Tuple

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
    
    def to_sql( self ) -> Tuple[str, Iterable[Any]]:
        return f'ALTER TABLE {self.name()} RENAME TO {self._new_name};', []