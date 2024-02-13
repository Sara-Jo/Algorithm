/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    if (n < 10) {
        if (n === 1 || n === 7) return true
        else return false
    }

    let sum = 0
    while (n > 0) {
        sum += (n % 10)**2
        n = Math.floor(n / 10)
    }

    if (sum === 1) return true

    return isHappy(sum)
};
