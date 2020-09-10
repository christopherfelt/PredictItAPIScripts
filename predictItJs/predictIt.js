class PredictIt {
  constructor(data) {
    this.data = data;
    this.markets = data["markets"];
  }

  get marketCount() {
    return this.markets.length;
  }

  get marketTitles() {
    return this.markets.map((x) => x.name);
  }

  getMarketsByKeyWord(keyWord) {
    const markets = this.markets;
    let results = [];
    for (let i = 0; i < markets.length; i++) {
      let market = markets[i];
      if (market.name.includes(keyWord)) {
        results.push(market);
      }
    }
    return results;
  }

  getMarketTitlesByKeyWord(keyWord) {
    const markets = this.markets;
    let results = [];
    for (let i = 0; i < markets.length; i++) {
      let market = markets[i];
      if (market.name.includes(keyWord)) {
        results.push(market.name);
      }
    }
    return results;
  }
}

// need to add a method that gets market by number of days remaining

export default PredictIt;
