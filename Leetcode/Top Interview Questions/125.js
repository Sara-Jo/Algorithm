/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const string = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, '')
    const arr = string.split('').reverse()
    
    return string === arr.join('')
};
