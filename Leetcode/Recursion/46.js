/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  let answer = [];

  function makePermutations(curr, list) {
    if (curr.length === nums.length) return answer.push(curr);

    for (let i = 0; i < list.length; i++) {
      makePermutations(
        [...curr, list[i]],
        list.filter((num, j) => i !== j)
      );
    }
  }

  makePermutations([], nums);

  return answer;
};
