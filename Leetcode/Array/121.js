/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min_price = Infinity;
  let answer = 0;

  for (price of prices) {
    if (price < min_price) min_price = price;
    else answer = Math.max(answer, price - min_price);
  }

  return answer;
};
