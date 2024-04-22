/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;

  let start = 0;
  let end = 1;
  let answer = 1;

  while (end < s.length) {
    let substring = s.slice(start, end + 1);
    let set = new Set(substring);
    if (end - start + 1 === set.size) {
      answer = Math.max(answer, end - start + 1);
      end++;
    } else {
      start++;
      end++;
    }
  }

  return answer;
};
