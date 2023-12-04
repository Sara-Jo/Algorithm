/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let answer = 0
    let minNum = 10001

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < minNum) {
            minNum = prices[i]
        } else if (prices[i] - minNum > answer) {
            answer = prices[i] - minNum
        }
    }

    return answer
};
