/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    const n = board.length
    const m = board[0].length
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            let liveCellCount = getLiveCellCount(board, i, j)

            if (board[i][j] === 1) {
                if (liveCellCount < 2 || liveCellCount > 3) board[i][j] = 3
            } else if (liveCellCount === 3) {
                board[i][j] = 2
            }
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (board[i][j] > 1) board[i][j] = 3 - board[i][j]
        }
    }
};

const getLiveCellCount = function(board, x, y) {
    const n = board.length
    const m = board[0].length
    const dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    const dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    let count = 0

    for (let i = 0; i < 8; i++) {
        let nx = x + dx[i]
        let ny = y + dy[i]
        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (board[nx][ny] === 1 || board[nx][ny] === 3) count++
        }
    } 

    return count
}
