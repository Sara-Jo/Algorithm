/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let answer = [];
  let tmp = 1;

  for (let i = 0; i < nums.length; i++) {
    answer.push(tmp);
    tmp *= nums[i];
  }

  tmp = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    answer[i] *= tmp;
    tmp *= nums[i];
  }

  return answer;
};
