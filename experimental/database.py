# This class talks to the database on behalf of the program. It's so
# each class doesn't need its own code to connect to the database.

#activate_this = "/home/nicrev2/28protons.com/stocks/28p_app/bin/activate_this.py"
#exec(open(activate_this).read(), dict(__file__=activate_this))

import json, pymysql
from config import *

class DBInterface:

    # When it's initialized, do nothing
    def __init__(self):
        #connection = self.connect()
        #self.test(connection)
        pass

    def connect(self):
        connection = pymysql.connect(host = host,
                                     user = user,
                                     password = password,
                                     db = db)
        return connection
    
    def test(self, connection):
        with connection.cursor() as cursor:
            sql = "select * from `test table`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    
    def fetchrecord(self, connection, sql):
        with connection.cursor() as cursor:
            sql = "select * from `test table`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)