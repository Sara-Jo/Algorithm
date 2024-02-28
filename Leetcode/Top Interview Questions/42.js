/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let l = 0
    let r = height.length - 1
    let left_max = 0, right_max = 0
    let answer = 0

    while(l <= r) {
        if (height[l] <= height[r]) {
            if (height[l] > left_max) left_max = height[l]
            else answer += left_max - height[l]
            l++
        } else {
            if (height[r] > right_max) right_max = height[r]
            else answer += right_max - height[r]
            r--
        }
    }

    return answer
};
