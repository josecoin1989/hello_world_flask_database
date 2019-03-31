"""
Author: José Antonio Domínguez González
Date: 31/03/2019
"""
import sqlite3
from sqlite3 import Error

from flask import Blueprint, jsonify

# Declare the blueprint which contains the end-points
database = Blueprint('database', __name__)


@database.route('/database/create/<database_name>')
def create_database(database_name):
    """
    Create a database
    :param database_name:
    :return:
    """
    try:

        # This new connection create the database
        conn = sqlite3.connect(database_name)

        # Return information everything is ok
        return 'Database {} created!'.format(database_name)
    except Error as e:
        return str(e)
    # Always close the connection
    finally:
        conn.close()


@database.route('/database/<database_name>/create/table/<table_name>')
def create_table(database_name, table_name):
    """
    Create a table in the database
    :param database_name:
    :param table_name:
    :return:
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_name)

        # If conn exits
        with conn:
            # Create a cursor
            cur = conn.cursor()

            # Execute the query
            cur.execute(
                "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT)".format(table_name))

        # Return information everything is ok
        return 'Table {} created in the database {} values (id,name)'.format(table_name, database_name)
    except Error as e:
        return str(e)
    # Always close the connection
    finally:
        conn.close()


@database.route('/database/<database_name>/drop/table/<table_name>')
def drop_table(database_name, table_name):
    """
    Drop a table in the database
    :param database_name:
    :param table_name:
    :return:
    """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS {}".format(table_name))

        return 'Table {} droped in the database {}'.format(table_name, database_name)
    except Error as e:
        return str(e)
    finally:
        conn.close()


@database.route('/database/<database_name>/insert/table/<table_name>/value/<value>')
def insert_value(database_name, table_name, value):
    """
    Insert a value in the table
    :param database_name:
    :param table_name:
    :param value:
    :return:
    """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO {} (name) VALUES  ('{}')".format(table_name, value))
        return 'Value {} inserted into {} '.format(value, table_name)
    except Error as e:
        return str(e)

    finally:
        conn.close()


@database.route('/database/<database_name>/table/<table_name>/values')
def get_values(database_name, table_name, ):
    """
    Get the values of the table
    :param database_name:
    :param table_name:
    :return:
    """
    try:
        conn = sqlite3.connect(database_name)

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM {}".format(table_name))

            # Fetchall return all the rows of the select
            rows = cur.fetchall()
        return jsonify(rows)
    except Error as e:
        return str(e)
    finally:
        conn.close()
