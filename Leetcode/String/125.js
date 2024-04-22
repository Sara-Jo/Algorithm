/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let temp = "";
  for (let i = 0; i < s.length; i++) {
    if ((s[i] >= "A" && s[i] <= "Z") || (s[i] >= "a" && s[i] <= "z"))
      temp += s[i].toLowerCase();
    if (s[i] >= "0" && s[i] <= "9") temp += s[i];
  }

  return temp === [...temp].reverse().join("");
};
