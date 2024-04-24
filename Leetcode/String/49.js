/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = new Map();

  strs.forEach((str) => {
    let sortedStr = [...str].sort().join("");
    if (map.has(sortedStr)) map.set(sortedStr, [...map.get(sortedStr), str]);
    else map.set(sortedStr, [str]);
  });

  return Array.from(map.values());
};
