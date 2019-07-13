import urllib.request
import json
import os
import io
from database import DBInterface
from api import *


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

    # Gets the symbols in JSON Format, then grabs each entry and
    # inserts it into the temp table.
    def get_new_symbols(self):

        website = 'https://cloud.iexapis.com/stable'
        iex_symbols = '/ref-data/iex/symbols'
        with urllib.request.urlopen(website + iex_symbols
                                    + public_api_token) as url:
            data = json.loads(url.read().decode())

        for entry in data:
            entry['name'].replace("'", "''")
            string = ("'" + str(entry['symbol'])
                      + "','" + str(entry['date'])
                      + "','" + str(entry['isEnabled']) + "'"
                      + '\n')
            sql = "insert into temp_symbol_list VALUES (" + string + ");"
            self.interface.execute_sql(sql)

    # Create a temporary table and dump the symbols in csv format into
    # it. Then update all of the records that have new data. Probably
    # delete old records if they're out of date by more than
    # a few days.
    def update_table(self, interface):
        sql = "CREATE TEMPORARY TABLE temp_symbol_list (symbol text, date text, isEnabled text);"
        self.interface.execute_sql(sql)

        self.get_new_symbols()

        sql = 'insert into symbol_list select * from temp_symbol_list where symbol not in (select symbol from symbol_list);'
        self.interface.execute_sql(sql)

        sql = 'update symbol_list a set symbol = b.symbol, date = b.date, "isEnabled" = b.isenabled, from temp_symbol_list b where b.date != a.date and a.symbol = b.symbol;'
        self.interface.execute_sql(sql)

        self.interface.commit_and_close_connection()

    def delete_old_symbols(self):
        pass
