/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const n = matrix.length
    const m = matrix[0].length
    let arr = []

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (matrix[i][j] === 0) arr.push([i, j])
        }
    }

    arr.forEach((a) => {
        let [i, j] = a
        for (let k = 0; k < m; k++) matrix[i][k] = 0
        for (let k = 0; k < n; k++) matrix[k][j] = 0
    })
};
