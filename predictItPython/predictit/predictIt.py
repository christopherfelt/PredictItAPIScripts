class PredictIt:
    def __init__(self, data):
        self.data = data
        self.markets = data["markets"]

    def get_market_count(self):
        return len(self.markets)

    def market_names(self):
        return self.markets.map(lambda x: x.name)

    def get_markets_by_keyword(self, keyword):
        result = []
        for market in self.markets:
            if keyword in market['name']:
                result.append(market)
        return result
    
    def get_markets_titles_by_keyword(self, keyword):
        result = []
        for market in self.markets:
            if keyword in market['name']:
                result.append(market['name'])
        return result
    
    def get_first_markets(self, num):
        result = []
        for i in range(0, num):
            result.append(self.markets[i])
        return result

    def get_market_by_id(self, id):
        return [market for market in self.markets if market['id']==id]

    def get_market_ids(self):
        return self.markets.map(lambda x: x.id)

    def get_market_contracts_by_id(self, id):
        market = self.get_market_by_id(id)
        return market[0]['contracts']

    # def get_
