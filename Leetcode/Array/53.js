/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let dp = [nums[0]];
  let max_sum = dp[0];

  for (let i = 1; i < nums.length; i++) {
    dp.push(Math.max(dp[i - 1] + nums[i], nums[i]));
    max_sum = Math.max(max_sum, dp[i]);
  }

  return max_sum;
};
