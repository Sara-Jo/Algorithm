/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let dict = {}

    nums.forEach((num) => {
        if (dict[num]) {
            dict[num]++
        } else {
            dict[num] = 1
        }
    })

    let keys = Object.keys(dict)
    keys.sort((a, b) => dict[b] - dict[a])
    return keys[0]
};
