# This class talks to the database on behalf of the program. It's so
# each class doesn't need its own code to connect to the database.

#activate_this = "/home/nicrev2/28protons.com/stocks/28p_app/bin/activate_this.py"
#exec(open(activate_this).read(), dict(__file__=activate_this))

import json, psycopg2
from config import *

class DBInterface:

    # When it's initialized, do nothing
    def __init__(self):
        #connection = self.connect()
        #self.test(connection)
        self.connection = ""
        self.cursor = ""

    def connect(self):
        connection_string = ("host='" + host + "' dbname='" + dbname + "' user='"
                      + user + "' password='" + password + "' connect_timeout=30")
        self.connection = psycopg2.connect(connection_string)
        self.cursor = self.connection.cursor()

    # Execute sql and returns the records pulled
    def fetch_records(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    # Just execute a query.
    def execute_sql(self, sql):
        self.cursor.execute(sql)

    def copy_records(self, table, records):
        try:
            #sql = "COPY " + table + " FROM STDIN (format csv)"
            #self.cursor.copy_expert(sql, records)
            self.cursor.copy_from(records, table)
        except Exception as e:
            print (e)

    def get_cursor(self):
        if (self.cursor != ""):
            return self.cursor

    # Commits all changes to the database. Will roll back if there is an error.
    # Reports if it succeeds or fails.
    def commit_to_database(self):
        try:
            self.connection.commit()
            return True
        except:
            self.connection.rollback()
            return False

    def close_database_connection(self):
        self.cursor.close()
        self.connection.close()

    def commit_and_close_connection(self):
        self.commit_to_database()
        self.close_database_connection()
    
    # Test method
    def test(self):
        sql = "select * from test_table;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(result)

#db = DBInterface()
#db.connect()
#db.test()