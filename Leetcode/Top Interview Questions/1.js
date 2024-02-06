/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length - 1; i++) {
        const index = nums.slice(i + 1, nums.length).indexOf(target - nums[i])
        if (index >= 0) return [i, i + index + 1]
    }
};
