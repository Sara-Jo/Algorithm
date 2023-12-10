/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let last = nums.length - 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (i + nums[i] >= last) {
      last = i;
    }
  }

  if (last === 0) {
    return true;
  } else {
    return false;
  }
};
