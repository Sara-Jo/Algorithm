/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (matrix, k) {
  let n = matrix.length;
  let left = matrix[0][0];
  let right = matrix[n - 1][n - 1];

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let count = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (matrix[i][j] <= mid) count++;
        else break;
      }
    }
    if (count < k) left = mid + 1;
    else right = mid - 1;
  }

  return left;
};
