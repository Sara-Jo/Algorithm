/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  let answer = [];

  function makeCombinations(arr) {
    if (arr.length === k) return answer.push(arr);

    for (let i = arr[arr.length - 1] + 1; i <= n; i++) {
      makeCombinations([...arr, i]);
    }
  }

  for (let i = 1; i <= n; i++) {
    makeCombinations([i]);
  }

  return answer;
};
