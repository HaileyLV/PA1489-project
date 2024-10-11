import pytest
import sqlite3

def db_connection():
    """_testing to connect the database_
    """
    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        yield cursor
            
def test_create_a_table ():
    """_testing to create a table on database
    """            
    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute ('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);''')
        conn.commit ()
        
        # Check if the table has been created
        table = cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';''').fetchone()
        assert table is not None, "Table has been created."
    
def test_drop_a_table ():
    """_test to drrop a table database_
    """
    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute ('''DROP TABLE IF EXISTS test;''')

        # Check if the table has been dropped
        table = cursor.execute('''SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';''').fetchone()
        assert table is None, "Table has been dropped."
    