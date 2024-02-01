/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const p = pattern.split('')
    const s_copy = s.split(' ')
    
    if (p.length !== s_copy.length) return false

    for (let i = 0; i < p.length; i++) {
        if (p.indexOf(p[i]) !== s_copy.indexOf(s_copy[i])) return false
    }

    return true
};
