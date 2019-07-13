import urllib.request
import json
import os
import datetime
from symbolvalidator import SymbolValidator
from api import *

# Processor class to process the data


class Processor:

    # When it's initialized, do nothing
    def __init__(self):
        pass

    # Takes in a list of tickers in comma separated format.
    def process(self, ticker, market=False):
        if market == False:
            validator = SymbolValidator()
            ticker = validator.check_symbols(ticker)

        # It magically breaks when this line isn't included and
        # I'm not going to spend the time to figure out why right
        # now. The url works without using capitals normally.
        ticker = ticker.upper()

        # Initialize the output variable so we can assign it in the
        # with statement.
        output = ""

        website = 'https://cloud.iexapis.com/stable/stock/'
        batch_request = 'market/batch?symbols='
        batch_types = '&types=quote'
        batch_token = '&token=' + public_api_token

        # Nab the json file from the online api and assign it to the
        # output variable.
        with urllib.request.urlopen(website + batch_request + ticker
                                    + batch_types + batch_token) as url:
            data = json.loads(url.read().decode())
            output = self.return_json(ticker, data, market=market)
        return output

    # Iterates through the list of stocks input by the user and
    # return the json of information that will be displayed to
    # the user. Will work if the list is only a single stock.
    def return_json(self, input_list, input_json, market=False):
        output = {}
        tickers = input_list.split(",")
        for stock in tickers:
            quote = input_json[stock]['quote']
            output[stock] = self.make_stock_entry(quote, stock,
                                                  market=market)
        return output

    # Gets the change and change percentage and converts it into
    # html that will make it suitable to display on the page in
    # the right format.
    #
    # Has option for an extension which changes the class names
    # of the positive, neutral, and negative spans.
    #
    # Also has option in the event that it's displaying market data,
    # which doesn't require the precise amount the representative
    # etf went up
    def process_change(self, change, change_percent, extension="", market=False):
        change_percent = round(change_percent * 100, 2)
        return_string = "<span class='"
        modifier = ""
        if (change_percent > 0):
            modifier = "+"
            return_string += "positive" + extension + "'>"
        elif (change_percent == 0):
            modifier = "+"
            return_string += "neutral" + extension + "'>"
        else:
            return_string += "negative" + extension + "'>"

        if market:
            return_string += (modifier + str(change_percent)
                              + "%</span>")
        else:
            return_string += " " + modifier + (str(change) + "("
                                               + modifier + str(change_percent)
                                               + "%)</span>")
        return return_string

    # The latest source variable in the json will contain some
    # strings that are too long, so this method shortens them.
    # Unused until later due to change in UI.
    def modify_latest_source(self, latest_source):
        new_source = latest_source
        if latest_source == 'IEX real time price':
            new_source = 'Real Time'
        elif latest_source == '15 minute delayed price':
            new_source = '15 Min Delay'
        return new_source

    # Processes the extended quote to return a line that will say
    # all of the stats that are required for extended prices.
    def process_extended_quote(self, quote):
        extended_price = quote['extendedPrice']
        extended_change = quote['extendedChange']
        extended_change_percent = quote['extendedChangePercent']
        price = ("<span class = 'price--extended'>"
                 + str(extended_price) + "</span>")
        change = self.process_change(extended_change,
                                     extended_change_percent,
                                     extension="--extended")
        return price + change

    # Calculates whether the market is open or if the market is in
    # pre or after market hours.
    def process_market_phase(self, quote):

        # Convert extended time into datetime format so we can pull
        # the information in a more convenient way. Also divide the
        # extended time by 1000 because it's in milliseconds, not
        # seconds.
        extended_time = (datetime.datetime.fromtimestamp(quote
                                                         ['extendedPriceTime']/1000))
        phase = ""
        current_day = datetime.datetime.now().day

        # Check pre-market hours and see if the extended time is
        # on the right day, otherwise set phase to after hours.
        if (extended_time.hour >= 5 and
            (extended_time.hour <= 6 and
             extended_time.minute < 31) and
                extended_time.day == current_day):
            phase = "Pre-market"
        else:
            phase = "After hours"

        # If the open time is today, and the close isn't today then
        # it must be market hours now.
        close_time = (datetime.datetime.fromtimestamp(quote
                                                      ['closeTime']/1000))
        open_time = (datetime.datetime.fromtimestamp(quote
                                                     ['openTime']/1000))
        if (open_time.day == current_day and
                close_time.day != current_day):
            return "market"

        # Return the calculated phase if market isn't open.
        return phase

    # Creates a stock entry in json format that will make up the
    # overall json file that will be returned.
    # It has an option for market data where it will only return
    # the symbol and the change because those are the only things
    # required.
    def make_stock_entry(self, quote, stock, market=False):
        if market:
            return {"symbol": str(quote['symbol']),
                    "change": self.process_change(quote['change'],
                                                  quote['changePercent'],
                                                  market=market)}
        return {"symbol": str(quote['symbol']),
                "company": str(quote['companyName']),
                "latestPrice": quote['latestPrice'],
                "change": self.process_change(quote['change'],
                                              quote['changePercent']),
                "extendedPriceTime": quote['extendedPriceTime'],
                "extendedQuote": self.process_extended_quote(quote),
                "marketPhase": self.process_market_phase(quote)}
