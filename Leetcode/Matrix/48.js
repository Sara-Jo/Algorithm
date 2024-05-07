/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  let n = matrix.length;
  let row = 0;

  while (row <= n / 2 - 1) {
    for (let i = row; i < n - 1 - row; i++) {
      let temp = matrix[i][n - 1 - row];
      matrix[i][n - 1 - row] = matrix[row][i];
      matrix[row][i] = matrix[n - 1 - i][row];
      matrix[n - 1 - i][row] = matrix[n - 1 - row][n - 1 - i];
      matrix[n - 1 - row][n - 1 - i] = temp;
    }
    row++;
  }
};
