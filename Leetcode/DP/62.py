class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #-------------1---------------
        # def factorial(n: int) -> int:
        #     result = 1
        #     for i in range(n, 1, -1):
        #         result *= i
        #     return result

        # fac_total = factorial(m + n - 2)
        # fac_m = factorial(m - 1)
        # fac_n = factorial(n - 1)
        
        # return fac_total // fac_m // fac_n

        #-------------2---------------
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

