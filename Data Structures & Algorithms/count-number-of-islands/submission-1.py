class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r, c)
                    islands+=1
        return islands

