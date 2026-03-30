class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        lvl = 0
        visited = set()
        q.append((0,0))
        while q:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                if (r,c) == (rows-1,cols-1):
                    return lvl
                if r+1 in range(rows) and c in range(cols) and grid[r+1][c]==0 and (r+1,c) not in visited:
                    q.append((r+1, c))
                    visited.add((r+1, c))
                if r-1 in range(rows) and c in range(cols) and grid[r-1][c] ==0 and (r-1,c) not in visited:
                    q.append((r-1, c))
                    visited.add((r-1, c))
                if r in range(rows) and c + 1 in range(cols) and grid[r][c+1] ==0 and (r, c + 1) not in visited:
                    q.append((r, c + 1))
                    visited.add((r, c +1))
                if r in range(rows) and c - 1 in range(cols) and grid[r][c-1] ==0 and (r, c - 1) not in visited:
                    q.append((r, c - 1))
                    visited.add((r, c-1))
            lvl+=1
        
        return -1
                       

            
