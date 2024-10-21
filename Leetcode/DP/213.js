/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const n = nums.length;

  if (n === 1) return nums[0];
  if (n === 2) return Math.max(nums[0], nums[1]);

  const dp1 = Array(n).fill(0);
  const dp2 = Array(n).fill(0);
  dp1[0] = nums[0];
  dp1[1] = nums[0];
  dp2[1] = nums[1];

  for (let i = 2; i < n - 1; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
  }

  for (let i = 2; i < n; i++) {
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i]);
  }

  return Math.max(...dp1, ...dp2);
};
