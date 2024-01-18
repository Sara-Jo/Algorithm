/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let answer = 0
    let right = 1
    let currArr = []
    let set = {}
    
    for (let left = 0; left < s.length; left++) {
        currArr = s.slice(left, right)
        set = new Set(currArr)
        while (currArr.length === set.size) {
            answer = Math.max(answer, right - left)
            currArr += s[right]
            set = new Set(currArr)
            right++
        }
    }

    return answer
};
