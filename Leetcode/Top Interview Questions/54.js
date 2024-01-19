/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let answer = []
    const n = matrix.length
    const m = matrix[0].length

    let direction = 0
    let top = 0
    let bottom = matrix.length - 1
    let left = 0
    let right = matrix[0].length - 1

    while (answer.length < n * m) {
        if (direction === 0) {
            for (let i = left; i <= right; i++) {
                answer.push(matrix[top][i])
            }
            top++
        } else if (direction === 1) {
            for (let i = top; i <= bottom; i++) {
                answer.push(matrix[i][right])
            }
            right--
        } else if (direction === 2) {
            for (let i = right; i >= left; i--) {
                answer.push(matrix[bottom][i])
            }
            bottom--
        } else {
            for (let i = bottom; i >= top; i--) {
                answer.push(matrix[i][left])
            }
            left++
        }
        direction = (direction + 1) % 4
    }

    return answer
};
