/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // row check
  for (let i = 0; i < 9; i++) {
    let map = new Map();
    for (let j = 0; j < 9; j++) {
      if (board[i][j] !== ".") {
        if (map.has(board[i][j])) return false;
        else map.set(board[i][j], 1);
      }
    }
  }

  // column check
  for (let i = 0; i < 9; i++) {
    let map = new Map();
    for (let j = 0; j < 9; j++) {
      if (board[j][i] !== ".") {
        if (map.has(board[j][i])) return false;
        else map.set(board[j][i], 1);
      }
    }
  }

  // sub-boxes check
  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
      let map = new Map();
      for (let k = 0; k < 3; k++) {
        for (let l = 0; l < 3; l++) {
          if (board[i + k][j + l] !== ".") {
            if (map.has(board[i + k][j + l])) return false;
            else map.set(board[i + k][j + l], 1);
          }
        }
      }
    }
  }

  return true;
};
