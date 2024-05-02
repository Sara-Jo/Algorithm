/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits.length === 0) return [];

  let answer = [];
  const letters = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
  };

  function makeCombination(count, s) {
    if (count === digits.length) return answer.push(s);

    for (letter of letters[digits[count]]) {
      makeCombination(count + 1, s + letter);
    }
  }

  makeCombination(0, "");

  return answer;
};
