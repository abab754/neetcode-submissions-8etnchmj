class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                # if r == rows-1 and c == cols-1:
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
                dp[rows-1][cols-1] = 1
        
        return dp[0][0]
