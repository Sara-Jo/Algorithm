/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    for (let i = 0; i < 9; i++) {
        let arr1 = []
        let arr2 = []
        for (let j = 0; j < 9; j++) {
            if (board[i][j] !== '.') {
                if (arr1.includes(board[i][j])) return false
                arr1.push(board[i][j])
            }
            if (board[j][i] !== '.') {
                if (arr2.includes(board[j][i])) return false
                arr2.push(board[j][i])
            }
        }
    }

    for (let i = 0; i < 9; i += 3) {
        for (let j = 0; j < 9; j += 3) {
            let arr = []
            for (let k = 0; k < 3; k++) {
                if((board[i][j + k]) !== '.') arr.push(board[i][j + k])
                if((board[i + 1][j + k]) !== '.') arr.push(board[i + 1][j + k])
                if((board[i + 2][j + k]) !== '.') arr.push(board[i + 2][j + k])
            }
            let set = new Set(arr)
            if (arr.length !== set.size) return false
        }
    }

    return true
};
