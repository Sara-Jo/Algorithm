/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
  let answer = [[]];

  function makeSubsets(index, arr) {
    if (arr.length === nums.length) return;

    for (let i = index; i < nums.length; i++) {
      if (i > index && nums[i] === nums[i - 1]) continue;
      answer.push([...arr, nums[i]]);
      makeSubsets(i + 1, [...arr, nums[i]]);
    }
  }

  nums.sort();
  makeSubsets(0, []);

  return answer;
};
