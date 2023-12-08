/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy = prices[0]
    let answer = 0

    for(let i = 1; i < prices.length; i++) {
      buy = Math.min(buy, prices[i])
      if (prices[i] > buy) {
          answer += prices[i] - buy
          buy = prices[i]
      }
    }

    return answer
};
