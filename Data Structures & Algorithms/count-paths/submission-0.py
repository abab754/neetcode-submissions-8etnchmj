class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        for i in range(n):
            dp[m-1][i] = 1
        
        def f(i, j):
            if i not in range(m) or j not in range(n):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = f(i+1, j) + f(i, j+1)
            return dp[i][j]
        
        return f(0, 0)