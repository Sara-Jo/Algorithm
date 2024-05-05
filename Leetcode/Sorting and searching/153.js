/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;
  let answer = Infinity;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);

    if (nums[mid] >= nums[left]) {
      answer = Math.min(answer, nums[left]);
      left = mid + 1;
    } else {
      answer = Math.min(answer, nums[mid]);
      right = mid - 1;
    }
  }

  return answer;
};
