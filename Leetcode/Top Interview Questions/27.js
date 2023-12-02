/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0

    nums.forEach((num, i) => {
        if (num === val) {
            nums[i] = 51
        } else {
            k++
        }
    })
    nums.sort((a, b) => a - b)

    return k
};
