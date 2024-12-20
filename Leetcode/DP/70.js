/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let dp = [0, 1, 2];

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 2] + dp[i - 1];
  }

  return dp[n];
};
