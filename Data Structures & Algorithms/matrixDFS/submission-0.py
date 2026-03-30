class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 1 or (r,c) in visited:
                return 0
            if (r,c) == (rows - 1, cols - 1):
                return 1
            visited.add((r,c))
            total = dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)
            visited.remove((r,c))
            return total

        return dfs(0, 0)