class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()
        visit = set()

        def addCell(r,c):
            if((r not in range(rows)) or (c not in range(cols)) or (grid[r][c] == 0) or (r,c) in visit):
                return
            visit.add((r,c))
            q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        if fresh == 0:
            return 0
        time = -1

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 1:
                    fresh-=1
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            time+=1
        if fresh == 0:
            return time
        return -1