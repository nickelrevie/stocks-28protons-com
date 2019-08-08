import urllib.request, json, os, datetime
from database import DBInterface

class SymbolValidator:

    # When it's initialized, do nothing
    def __init__(self):
        self.interface = self.get_connection()

    # Returns the database connection
    def get_connection(self):
        interface = DBInterface()
        interface.connect()
        return interface

    # Checks whether the input symbols exist and returns existing ones
    def check_symbols(self,symbols):
        good_symbols = []
        input = symbols.split(",")
        for symbol in input:
            sql = "select symbol from symbol_list where symbol = '" + symbol.upper() + "';"
            result = self.interface.fetch_records(sql)
            if result != []:
                good_symbols.append(symbol)
        return ','.join(good_symbols)