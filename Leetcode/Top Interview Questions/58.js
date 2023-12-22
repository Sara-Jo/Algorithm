/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let end = s.length - 1
    
    while (s[end] === ' ' && end >= 0) {
        end--
    }
    
    let start = end
    while (s[start] !== ' ' && start >= 0){
        start--
    }
    return end - start
};
