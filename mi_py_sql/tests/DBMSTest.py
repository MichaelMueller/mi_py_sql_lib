# pip
from mi_py_test.AbstractTest import AbstractTest
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Table import Table


class DBMSTest(AbstractTest):    
    def __init__(self, instance:DBMS) -> None:        
        super().__init__()        
        self._instance = instance
        
    async def _exec(self):        
        # make sure the test database does not exist before start testing
        test_db_name = "6c4ad2db-cb84-40d7-abf7-a3aafab11e82" # for the name a uuid is used to not collide with other databases        
        self._assert( await self._instance.drop_database( test_db_name ) in [True, False], "Test database has been dropped before test start" )

        # create user/group database as test        
        db = await self._instance.create_database( test_db_name )
        schema = await db.schema()
        
        # create user table
        users_table_cols = [
            schema.create_integer_column( "id" ),
            schema.create_string_column ( "name", 1275 ),
            schema.create_string_column ( "hp", 1275   ),
            schema.create_integer_column( "is_admin"   ) ]
        
        schema.create_table( "users", users_table_cols, primary_keys=["id"], unique_keys=["name"] )
        table = await schema.table("users")
        self._assert( isinstance( table, Table ), "users database has been created" )
                
        # create groups table
        groups_table_cols = [
            schema.create_integer_column( "id" ),
            schema.create_string_column ( "name", 1275 ),
            schema.create_integer_column( "is_admin"   ) ]
        
        schema.create_table( "users", groups_table_cols, primary_keys=["id"], unique_keys=["name"] )
        table = await schema.table("users")
        self._assert( isinstance( table, Table ), "users database has been created" )