/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  strs = strs.sort((a, b) => a.length - b.length);

  for (let i = strs[0].length; i > 0; i--) {
    const check = strs[0].slice(0, i);

    let j = 1;
    while (j < strs.length) {
      if (strs[j].slice(0, i) !== check) {
        break;
      }
      j++;
    }

    if (j == strs.length) {
      return check;
    }
  }
  return "";
};
