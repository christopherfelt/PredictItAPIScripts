import requests
import json
import pprint
from predictit.predictIt import PredictIt

# r = requests.get("https://www.predictit.org/api/marketdata/all/")

# json = json.dumps(r.json())

# market_data = open("marketdata.json", "w+")
# market_data.write(json)
# market_data.close()
with open('marketdata.json') as f:
    market_data = json.load(f)

p = PredictIt(market_data)

# print(p.get_markets_by_keyword('party'))
# print(p.get_first_markets(1)[0]['id'])
pprint.pprint(p.get_market_by_id(2721)[0]['contracts'])