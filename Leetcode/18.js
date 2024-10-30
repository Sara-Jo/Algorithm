/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
  const n = nums.length;
  if (n < 4) return [];

  nums = nums.sort((a, b) => a - b);
  let answer = [];
  for (let i = 0; i < n - 3; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    for (let j = i + 1; j < n - 2; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) continue;

      let left = j + 1;
      let right = n - 1;
      while (left < right) {
        const totalSum = nums[i] + nums[j] + nums[left] + nums[right];

        if (totalSum === target) {
          answer.push([nums[i], nums[j], nums[left], nums[right]]);

          while (left < right && nums[left] === nums[left + 1]) {
            left++;
          }
          while (left < right && nums[right] === nums[right - 1]) {
            right--;
          }

          left++;
          right--;
        } else if (totalSum < target) {
          left++;
        } else {
          right--;
        }
      }
    }
  }

  return answer;
};
