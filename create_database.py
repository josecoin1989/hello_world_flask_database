import sqlite3
from sqlite3 import Error


def create_database(dbfile):
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(dbfile)

        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_database("pythonsqlite.db")