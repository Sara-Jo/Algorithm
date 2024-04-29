/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (s.length === 1) return s;

  let answer = s[0];
  let longest = 1;

  for (let i = 0; i < s.length - 1; i++) {
    for (let j = i + 1; j < s.length; j++) {
      if (j - i < longest || s[i] !== s[j]) continue;

      if (isPallindrome(s, i, j)) {
        answer = s.slice(i, j + 1);
        longest = j - i;
      }
    }
  }
  return answer;
};

let isPallindrome = function (str, start, end) {
  while (start < end) {
    if (str[start] !== str[end]) return false;
    start++;
    end--;
  }
  return true;
};
