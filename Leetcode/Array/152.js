/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  if (nums.length === 1) return nums[0];

  let maxProd = nums[0];
  let minProd = nums[0];
  let answer = nums[0];

  for (let i = 1; i < nums.length; i++) {
    let tempMax = Math.max(maxProd * nums[i], minProd * nums[i], nums[i]);
    let tempMin = Math.min(maxProd * nums[i], minProd * nums[i], nums[i]);
    maxProd = tempMax;
    minProd = tempMin;
    answer = Math.max(maxProd, answer);
  }

  return answer;
};
