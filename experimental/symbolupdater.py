import urllib.request, json, os, io
from database import DBInterface

class SymbolUpdater:

    # When it's initialized, connect to the database
    def __init__(self):
        self.interface = self.get_connection()

    # Initiates the process to check whether the input symbols exist
    def update_symbols(self):
        self.update_table(self.interface)

    # Returns the database connection
    def get_connection(self):
        interface = DBInterface()
        interface.connect()
        return interface

    # Gets the symbols in JSON Format, converts it into a csv StringIO
    # object and then returns it.
    def get_new_symbols(self):
        with urllib.request.urlopen("https://api.iextrading.com/"
            + "1.0/ref-data/symbols") as url:
            data = json.loads(url.read().decode())

        for entry in data:
            entry['name'].replace("'", "''")
            string = ("'" + str(entry['symbol'])
                    + "','" + str(entry['name'].replace("'", "''"))
                    + "','" + str(entry['date'])
                    + "','" + str(entry['isEnabled'])
                    + "','" + str(entry['type'])
                    + "','" + str(entry['iexId']) + "'"
                      + '\n')
            sql = "insert into temp_symbol_list VALUES (" + string + ");"
            self.interface.execute_sql(sql)

    # Create a temporary table and dump the symbols in csv format into
    # it. Then update all of the records that have new data. Probably
    # delete old records if they're out of date by more than
    # a few days.
    def update_table(self, interface):
        sql = "CREATE TEMPORARY TABLE temp_symbol_list (symbol text, name text, date text, isEnabled text, type text, iexId int);"
        self.interface.execute_sql(sql)

        #self.interface.copy_records("temp_symbol_list", symbols)
        #sql = "insert into temp_symbol_list VALUES ('YETI','YETI Holdings Inc.','2019-03-14','True','cs','11574');"
        #self.interface.execute_sql(sql)
        self.get_new_symbols()

        sql = 'select * from temp_symbol_list;'
        result = self.interface.fetch_records(sql)
        print(result)

        sql = 'insert into symbol_list select * from temp_symbol_list where iexId not in (select "iexId" from symbol_list);'
        self.interface.execute_sql(sql)

        sql = 'update symbol_list a set symbol = b.symbol, name = b.name, date = b.date, "isEnabled" = b.isenabled, type = b.type, "iexId" = b.iexid from temp_symbol_list b where b.date != a.date;'
        self.interface.execute_sql(sql)

        self.interface.commit_and_close_connection()

    def delete_old_symbols(self):
        pass