/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let start = 0;
  let end = height.length - 1;
  let answer = 0;

  while (start < end) {
    let amount = (end - start) * Math.min(height[start], height[end]);
    answer = Math.max(answer, amount);
    if (height[start] > height[end]) end--;
    else start++;
  }

  return answer;
};
