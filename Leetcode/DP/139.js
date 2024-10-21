/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  const dp = Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (const word of wordDict) {
      const start = i - word.length;
      if (
        start >= 0 &&
        dp[start] &&
        s.substring(start, start + word.length) === word
      ) {
        dp[i] = true;
        break;
      }
    }
  }

  return dp[s.length];
};
