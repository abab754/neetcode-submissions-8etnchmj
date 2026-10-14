class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        stop = False
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c))
                    stop = True
                    break
            if stop:
                break

        shared = defaultdict(int)
        visit = set()
        dirs = [[1,0], [-1,0], [0, 1], [0, -1]]
        res = 0
        while q:
            r, c = q.popleft()
            if (r, c) in visit:
                continue
            if (r, c) not in shared:
                res+=4
            elif (r, c) in shared:
                res += (4 - (shared[(r,c)] * 2))
            else:
                shared[(r, c)] +=1
            visit.add((r,c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                    shared[(nr, nc)]+=1
                    q.append((nr, nc))
        return res

            