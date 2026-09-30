class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n+1)] for i in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for r in range(m-2, -1, -1):
            dp[r][n-1] += grid[r][n-1] + dp[r+1][n-1]

        for c in range(n-2, -1, -1):
            dp[m-1][c] += grid[m-1][c] + dp[m-1][c+1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
            