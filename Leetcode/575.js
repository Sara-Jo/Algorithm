/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function (candyType) {
  const half = Math.floor(candyType.length / 2);
  const candySet = new Set([...candyType]);
  return candySet.size >= half ? half : candySet.size;
};
