import urllib.request, json, os, datetime, io, csv
from database import DBInterface


class SymbolUpdater:

    # When it's initialized, do nothing
    def __init__(self):
        pass

    # Initiates the process to check whether the input symbols exist
    def update_symbols(self):
        symbols = self.get_new_symbols()
        connection = self.get_connection()
    
    # Returns the database connection
    def get_connection(self):
        database = DBInterface()
        connection = database.connect()
        return connection

    # Gets the symbols in JSON Format, converts it into a csv
    # StringIO object and then returns it.
    def get_new_symbols(self):
        with urllib.request.urlopen("https://api.iextrading.com/"
            + "1.0/ref-data/symbols") as url:
            data = json.loads(url.read().decode())
        
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        for entry in data:
            string = (entry['symbol']
                      + "," + entry['name']
                      + "," + entry['date']
                      + "," + entry['isEnabled']
                      + "," + entry['type']
                      + "," + entry['iexId'])
            writer.writerow(string)
        return output
    
    # Create a temporary table and dump the symbols in csv format
    # into it. Then update all of the records that have new data.
    # Probably delete old records if they're out of date by more
    # than a few days.
    def update_table(self, connection):
        pass