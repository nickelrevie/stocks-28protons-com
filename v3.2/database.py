# This class talks to the database on behalf of the program. It's so
# each class doesn't need its own code to connect to the database.

#activate_this = "/home/nicrev2/28protons.com/stocks/28p_app/bin/activate_this.py"
#exec(open(activate_this).read(), dict(__file__=activate_this))

import json
import pymysql
from config import *


class DBInterface:

    # When it's initialized, do nothing
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db=db)
        return connection

    def fetch_records(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute_sql(self, sql):
        self.cursor.execute(sql)

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
        self.connection.close()

    def commit_and_close_connection(self):
        self.commit_to_database()
        self.close_database_connection()
