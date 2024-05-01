/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  let answer = [];

  function makeParenthesis(p, l, r) {
    if (r === n) return answer.push(p);

    if (l < n) makeParenthesis(p + "(", l + 1, r);
    if (r < l) makeParenthesis(p + ")", l, r + 1);
  }

  makeParenthesis("(", 1, 0);

  return answer;
};
