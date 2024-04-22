/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let s_arr = [...s];
  let t_arr = [...t];
  return s_arr.sort().join() === t_arr.sort().join();
};
