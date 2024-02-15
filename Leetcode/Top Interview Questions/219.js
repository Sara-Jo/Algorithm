/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const window = new Set()

    for (let i = 0; i < nums.length; i++) {
        if (i > k) {
            window.delete(nums[i - k - 1])
        }
        if (window.has(nums[i])) {
            return true
        }
        window.add(nums[i])
    }
    return false
};
