/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1) return s;

  const rows = new Array(numRows).fill("");
  let direction = 1;
  let currentRow = 0;

  for (const char of s) {
    rows[currentRow] += char;
    currentRow += direction;

    if (currentRow === 0 || currentRow === numRows - 1) {
      direction = -direction;
    }
  }

  return rows.join("");
};
