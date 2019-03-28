from flask import Blueprint, jsonify
import sqlite3
from sqlite3 import Error

database = Blueprint('database', __name__)


@database.route('/database/create/<database_name>')
def create_database(database_name):
    """ create a database connection to a database that resides
            in the memory
        """
    try:
        conn = sqlite3.connect(database_name)
        return 'Database {} created!'.format(database_name)
    except Error as e:
        return(e)
    finally:
        conn.close()

@database.route('/database/<database_name>/create/table/<table_name>')
def create_table(database_name, table_name):
    """ create a database connection to a database that resides
            in the memory
        """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT)".format(table_name))
        return 'Table {} created in the database {} values (id,name)'.format(table_name,database_name)
    except Error as e:
        return(e)
    finally:
        conn.close()

@database.route('/database/<database_name>/drop/table/<table_name>')
def drop_table(database_name, table_name):
    """ create a database connection to a database that resides
            in the memory
        """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS {}".format(table_name))
        return 'Table {} droped in the database {}'.format(table_name,database_name)
    except Error as e:
        return(e)
    finally:
        conn.close()

@database.route('/database/<database_name>/insert/table/<table_name>/value/<value>')
def insert_value(database_name, table_name, value):
    """ create a database connection to a database that resides
            in the memory
        """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO {} (name) VALUES  ('{}')".format(table_name,value))
        return 'Value {} inserted into {} '.format(value,table_name)
    except Error as e:
        return(e)
    finally:
        conn.close()

@database.route('/database/<database_name>/table/<table_name>/values')
def get_values(database_name, table_name,):
    """ create a database connection to a database that resides
            in the memory
        """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM {}".format(table_name))

            rows = cur.fetchall()
        return jsonify(rows)
    except Error as e:
        return(e)
    finally:
        conn.close()

