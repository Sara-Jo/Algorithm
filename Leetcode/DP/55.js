/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  //   const n = nums.length;
  //   const dp = Array(n).fill(false);
  //   dp[0] = true;

  //   for (let i = 0; i < n; i++) {
  //     const maxJump = nums[i];
  //     if (!dp[i]) continue;

  //     for (let j = 1; j <= maxJump; j++) {
  //       if (i + j < n) {
  //         dp[i + j] = true;
  //         if (i + j === n - 1) return true;
  //       }
  //     }
  //   }

  //   return dp[n - 1];

  let m = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > m) return false;

    m = Math.max(m, i + nums[i]);
  }

  return true;
};
