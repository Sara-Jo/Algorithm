/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  const dp = Array(text1.length).fill(0);
  let answer = 0;

  for (const c of text2) {
    let currLength = 0;
    for (let i = 0; i < text1.length; i++) {
      if (currLength < dp[i]) {
        currLength = dp[i];
      } else if (c === text1[i]) {
        dp[i] = currLength + 1;
        answer = Math.max(answer, currLength + 1);
      }
    }
  }

  return answer;
};
