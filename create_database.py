"""
Author: José Antonio Domínguez González
Date: 31/03/2019
"""
import sqlite3
from sqlite3 import Error


def create_database(dbfile):
    """
    Create a database
    :param dbfile:
    :return:
    """
    try:
        conn = sqlite3.connect(dbfile)

        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_database("put_a_name_here.db")