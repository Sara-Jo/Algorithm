/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let map = {};
  let start = 0;
  let maxFreq = 0;
  let longest = 0;

  for (let end = 0; end < s.length; end++) {
    map[s[end]] = (map[s[end]] || 0) + 1;
    maxFreq = Math.max(maxFreq, map[s[end]]);

    if (end - start + 1 - maxFreq > k) {
      map[s[start]]--;
      start++;
    } else {
      longest = Math.max(longest, end - start + 1);
    }
  }

  return longest;
};
