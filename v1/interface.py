import sys, json
from processor import Processor

# Try to process the input, otherwise print an error and exit.
try:
    processor = Processor()

    # Takes the input information, which is a list of stocks to get
    # via api in json format, process it via the Processor and
    # assign the output to the variable named result.
    result = processor.process(sys.argv[1])
except:
    print("ERROR")

    # Technically, I think the print statement exits the program
    # or at least the index.php will only receive the data from the
    # first print statement so the sys.exit doesn't matter.
    sys.exit(1)

# Generate new json to send back to PHP containing all the stock info
print (json.dumps(result))