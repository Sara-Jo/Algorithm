/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  let m = matrix.length;
  let n = matrix[0].length;

  function setZeros(x, y) {
    for (let i = 0; i < m; i++) matrix[i][y] = 0;
    for (let i = 0; i < n; i++) matrix[x][i] = 0;
  }

  let zeros = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === 0) zeros.push([i, j]);
    }
  }

  for (let i = 0; i < zeros.length; i++) {
    let [x, y] = zeros[i];
    setZeros(x, y);
  }

  return matrix;
};
