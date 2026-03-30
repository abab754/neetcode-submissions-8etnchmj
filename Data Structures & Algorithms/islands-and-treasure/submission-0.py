class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        time = 0
        visit =set()

        def addCell(r,c):
            if ((r not in range(rows)) or (c not in range(cols)) or (grid[r][c] == -1) or ((r,c) in visit)):
                return
            visit.add((r,c))
            q.append((r,c))


        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        while q:
            for i in range(len(q)):
                cell = q.popleft()
                r, c = cell[0], cell[1]
                grid[r][c] = time
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            time+=1