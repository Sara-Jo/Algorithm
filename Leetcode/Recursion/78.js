/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let answer = [[]];

  function makeSubsets(arr, index) {
    if (arr.length === nums.length) return;

    for (let i = index; i < nums.length; i++) {
      arr.push(nums[i]);
      answer.push([...arr]);
      makeSubsets(arr, i + 1);
      arr.pop();
    }
  }

  for (let i = 0; i < nums.length; i++) {
    answer.push([nums[i]]);
    makeSubsets([nums[i]], i + 1);
  }

  return answer;
};
