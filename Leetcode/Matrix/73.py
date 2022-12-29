class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))

        for zero in zeroes:
            x, y = zero
            for k in range(len(matrix[0])):
                matrix[x][k] = 0
            for k in range(len(matrix)):
                matrix[k][y] = 0
                