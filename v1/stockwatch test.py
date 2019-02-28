import urllib.request, json, os

base_dir = os.path.dirname(os.path.abspath(__file__))

with urllib.request.urlopen("https://api.iextrading.com/1.0/stock/aapl/batch?types=quote,news,chart&range=1m") as url:
    data = json.loads(url.read().decode())
    # json_path = base_dir + "/testjson.json"
    # with open (json_path, "w") as jsonfile:
    #     json.dump(data, jsonfile)
    print(data)