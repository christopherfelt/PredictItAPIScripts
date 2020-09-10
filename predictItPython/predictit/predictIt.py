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

    