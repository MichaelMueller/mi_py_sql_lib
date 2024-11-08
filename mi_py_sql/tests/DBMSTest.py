# pip
from mi_py_test.AbstractTest import AbstractTest
# local
from ..interfaces.DBMS import DBMS
from ..interfaces.Database import Database
from ..interfaces.Table import Table
from ..interfaces.CreateTable import CreateTableQuery


class DBMSTest(AbstractTest):    
    def __init__(self, instance:DBMS) -> None:        
        super().__init__()        
        self._instance = instance
        self._test_db_name = "6c4ad2db-cb84-40d7-abf7-a3aafab11e82" # for the name a uuid is used to not collide with other databases        

    async def _tidy_up_if_needed(self) -> None:
        # tidy up is called as part of the testing but twice (before _exec and after _exec)
        self._print(f'Removing test database if it exists')
        await self._instance.drop_database( self._test_db_name ).if_exists().exec()
        await self._instance.disconnect()
    
    async def _exec(self):    
        # create test database
        db:Database = await self._instance.create_database( self._test_db_name ).exec()    
        schema = await db.schema()
        
        # create user database
        await schema.create_table_query("users_wrong_name") \
            .int_primary_key_col("id", auto_increment=True) \
            .string_col("name", max_length=1275, unique=True, nullable=False) \
            .string_col("hp", max_length=1275, unique=False, nullable=False) \
            .int_col("is_admin", unique=False, nullable=False, default_value=0) \
            .exec()
        
        self._assert( await schema.table_exists("users_wrong_name"), "table 'users_wrong_name' exists")
        
        # create user table
        
        # make sure the test database does not exist before start testing
        
        # self._assert( await self._instance.drop_database( test_db_name ) in [True, False], "Test database has been dropped before test start" )

        # # create user/group database as test        
        # db = await self._instance.create_database( test_db_name )
        # schema = await db.schema()
        
        # # create user table
        # users_table_cols = [
        #     schema.create_integer_column( "id" ),
        #     schema.create_string_column ( "name", 1275 ),
        #     schema.create_string_column ( "hp", 1275   ),
        #     schema.create_integer_column( "is_admin"   ) ]
        
        # schema.create_table( "users", users_table_cols, primary_keys=["id"], unique_keys=["name"] )
        # table = await schema.table("users")
        # self._assert( isinstance( table, Table ), "users database has been created" )
                
        # # create groups table
        # groups_table_cols = [
        #     schema.create_integer_column( "id" ),
        #     schema.create_string_column ( "name", 1275 ),
        #     schema.create_integer_column( "is_admin"   ) ]
        
        # schema.create_table( "users", groups_table_cols, primary_keys=["id"], unique_keys=["name"] )
        # table = await schema.table("users")
        # self._assert( isinstance( table, Table ), "users database has been created" )