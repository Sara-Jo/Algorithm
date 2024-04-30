/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = new Map();

  strs.forEach((str) => {
    let sorted = [...str].sort().join("");
    if (map.has(sorted)) map.set(sorted, [...map.get(sorted), str]);
    else map.set(sorted, [str]);
  });

  return [...map.values()];
};
