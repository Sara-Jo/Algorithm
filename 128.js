/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0) return 0

    let s = new Set()
    let answer = 1

    for (let i = 0; i < nums.length; i++) {
        s.add(nums[i])
    }

    for (const val of s.values()) {
        if (!s.has(val - 1) && s.has(val + 1)) {
            let k = 1
            while (s.has(val + k)) k++
            answer = Math.max(answer, k)
        }
    }

    return answer
};
