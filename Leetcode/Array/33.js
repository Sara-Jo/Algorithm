/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (nums[mid] === target) return mid;
    if (nums[start] <= nums[mid]) {
      // if the left side is sorted
      if (nums[start] <= target && target < nums[mid])
        end = mid - 1; // if the target is on the left side
      else start = mid + 1;
    } else {
      // if the right side is sorted
      if (target > nums[mid] && target <= nums[end])
        start = mid + 1; // if the target is on the right side
      else end = mid - 1;
    }
  }

  return -1;
};
