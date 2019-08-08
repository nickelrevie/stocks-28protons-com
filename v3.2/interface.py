import sys
import json
from processor import Processor

# Try to process the input, otherwise print an error and exit.
error_msg = ""
try:
    error_msg="error: processor fail"
    processor = Processor()
    error_msg="error: input fail"
    input = sys.argv[1]
    error_msg="error: process fail"
    if input == "marketdata":
        error_msg="error: market fail"
        result = processor.process("dia,spy,qqq", market=True)
    else:
        # Takes the input information, which is a list of stocks to get
        # via api in json format, process it via the Processor and
        # assign the output to the variable named result.
        result = processor.process(input)
    
    # Generate new json to send back to PHP containing all the stock info
    print(json.dumps(result))
except:
    print(json.dumps(error_msg))

    # Technically, I think the print statement exits the program
    # or at least the index.php will only receive the data from the
    # first print statement so the sys.exit doesn't matter.
    #sys.exit(1)