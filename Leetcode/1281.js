/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  n = n.toString();
  let productOfDigits = 1;
  let sumOfDigits = 0;

  for (let i = 0; i < n.length; i++) {
    const num = Number(n[i]);
    productOfDigits *= num;
    sumOfDigits += num;
  }

  return productOfDigits - sumOfDigits;
};
