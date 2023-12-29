/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const symbols = [
        [1, 'I'],
        [4, 'IV'],
        [5, 'V'],
        [9, 'IX'],
        [10, 'X'],
        [40, 'XL'],
        [50, 'L'],
        [90, 'XC'],
        [100, 'C'],
        [400, 'CD'],
        [500, 'D'],
        [900, 'CM'],
        [1000, 'M']
    ]
    symbols.reverse()

    let answer = ''
    for (let i = 0; i < symbols.length; i++) {
        const count = Math.floor(num / symbols[i][0])
        for (let j = 0; j < count; j++) {
            answer += symbols[i][1]
        }
        num -= count * symbols[i][0]
    }
    return answer
};
