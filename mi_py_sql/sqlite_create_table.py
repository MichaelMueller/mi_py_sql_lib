from typing import Any, Iterable, TYPE_CHECKING

# local
if TYPE_CHECKING:
    from mi_py_sql.sqlite_database import SqliteDatabase    
from mi_py_sql import CreateTable

class SqliteCreateTable(CreateTable):
    """SQLite-specific implementation of CreateTable."""

    def __init__(self, database:"SqliteDatabase", table_name:str) -> None:
        super().__init__(database, table_name)
    
    def database(self) -> "SqliteDatabase":
        return super().database()
    
    async def exec( self, args:Iterable[Any]=[] ) -> "SqliteDatabase":
        await super().exec( args )
        return self.database()

    def to_sql(self) -> str:
        """
        Generate the SQL for creating a table.
        """
        columns = []
        type_map = { int: "INTEGER", float: "REAL", str: "TEXT", bytes: "BLOB" }
        
        for name, attributes in self._columns.items():
            col_def = [name]
            col_type = type_map.get(attributes["type"], "TEXT")
            col_def.append(col_type)
            
            if attributes.get("auto_increment", False):
                col_def.append("AUTO INCREMENT")
            if attributes.get("primary_key", False):
                col_def.append("PRIMARY KEY")
            if attributes.get("unique", False):
                col_def.append("UNIQUE")
            if "default_value" in attributes and attributes["default_value"] is not None:
                col_def.append(f"DEFAULT {self._format_value(attributes['default_value'])}")
            if "foreign_table" in attributes and "foreign_col" in attributes:
                col_def.append(
                    f"REFERENCES {attributes['foreign_table']}({attributes['foreign_col']})"
                )
            
            columns.append(" ".join(col_def))
        
        if_not_exists = " IF NOT EXISTS" if self._if_not_exists else ""
        columns_sql = ", ".join(columns)
        return f"CREATE TABLE{if_not_exists} {self._name} ({columns_sql});"
        
    @staticmethod
    def _format_value(value: Any) -> str:
        """
        Format values for SQL (e.g., strings and bytes).
        """
        if isinstance(value, str):
            return f"'{value}'"
        if isinstance(value, bytes):
            return f"X'{value.hex()}'"
        if value is None:
            return "NULL"
        return str(value)
