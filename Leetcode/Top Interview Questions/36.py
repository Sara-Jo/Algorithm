class Solution:
    def check(self, arr):
        for x in arr:
            if x == '.':
                continue
            if arr.count(x) != 1:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            if not self.check(board[i]):
                return False
        
        # check columns
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(board[j][i])
            if not self.check(tmp):
                return False

        # check sub-boxes
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                tmp = []
                for k in range(3):
                    for l in range(3):
                        tmp.append(board[i + k][j + l])
                if not self.check(tmp):
                    return False

        return True



