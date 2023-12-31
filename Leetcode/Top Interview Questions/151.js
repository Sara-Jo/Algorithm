/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let arr = s.split(" ");
  arr.reverse();

  let answer = "";

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "") continue;
    if (answer.length > 0) answer += " ";
    answer += arr[i];
  }

  return answer;
};
