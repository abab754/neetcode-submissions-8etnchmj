class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque([(r,c)])
            grid[r][c] = "0"

            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
            
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        return res