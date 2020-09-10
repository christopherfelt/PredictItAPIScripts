import Axios from "axios";
import fs from "fs";
import PredictIt from "./predictIt.js";

import marketData from "./marketdata.js";

// const apiAll = Axios.create({
//   baseURL: "https://www.predictit.org/api/marketdata/all/",
// });

// async function getMarketData() {
//   let data = await apiAll.get("");
//   fs.appendFile("marketdata.json", JSON.stringify(data.data), function (err) {
//     if (err) throw err;
//   });
// }

// getMarketData();

const predict = new PredictIt(marketData);

// console.log(predict.marketCount);
// console.log(predict.marketTitles);
console.log(predict.getMarketsByKeyWord("party"));
