import pytest
import sqlite3

# define a reusable setup for testing
@pytest.fixture
def db_connection():
    """_connect to the database: orders.db_
    """
    con = sqlite3.connect ("orders.db")
    cur = con.cursor()
    yield cur
    con.close ()

def table_exist(db_connection, table_name):
    """_test if table exist in database_

    Args:
        db_connection (_function test database_): _function name_
    """
    table = (db_connection.execute('''SELECT name FROM sqlite_master \
        WHERE type = 'table' AND name= ? ;'''), (table_name)).fetchone()    

def test_table_orders_exist (db_connection):
    """_Test if table orders exist_
    """
    assert table_exist(db_connection, 'abd') is not None, "Table orders exist in the database"
