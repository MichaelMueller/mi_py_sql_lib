# built-in imports
from typing import Any, Union, Optional, TYPE_CHECKING
import inspect
# local imports
if TYPE_CHECKING:
    from mi_py_sql import Database
from mi_py_sql import Query, Database

class CreateTable(Query):
    """ fluent interface for creating a table """
    
    def __init__(self, database:"Database", name:str) -> None:
        super().__init__()
        self._database = database
        self._name = name
        
        self._if_not_exists = None        
        self._columns = {}
        self._curr_name = None
        
    def database(self) -> "Database":
        return self._database
                     
    def int_auto_increment_pk( self, name:str ) -> "CreateTable":
        self._curr_name = name
        self._columns[name] = { "type": int, "auto_increment": True, "primary_key": True }
        return self
    
    def int(self, name:str ) -> "CreateTable":
        self._curr_name = name
        self._columns[name] = { "type": int }
        return self
    
    def float( self, name:str ) -> "CreateTable":        
        self._curr_name = name
        self._columns[name] = { "type": float }
        return self
            
    def string( self, name:str, max_length:int ) -> "CreateTable":
        self._curr_name = name
        self._columns[name] = { "type": str, "max_length": max_length }
        return self
    
    def blob( self, name:str, max_length:int ) -> "CreateTable":
        self._curr_name = name
        self._columns[name] = { "type": bytes, "max_length": max_length }
        return self
    
    def default_value( self, default_value:Union[int, float, str, bytes, None]=None ) -> "CreateTable":
        self._columns[self._curr_name]["default_value"] = default_value
        return self
            
    def unique( self, unique:bool=True ) -> "CreateTable":             
        self._columns[self._curr_name]["unique"] = unique
        return self

    def primary_key( self, primary_key:bool=True ) -> "CreateTable":       
        self._columns[self._curr_name]["primary_key"] = primary_key
        return self

    def if_not_exists( self, if_not_exists:bool=True ) -> "CreateTable":       
        self._if_not_exists = if_not_exists
        return self
        
    def references( self, foreign_table:str, foreign_col:str ) -> "CreateTable":     
        self._columns[self._curr_name]["foreign_table"] = foreign_table    
        self._columns[self._curr_name]["foreign_col"] = foreign_col    
        return self