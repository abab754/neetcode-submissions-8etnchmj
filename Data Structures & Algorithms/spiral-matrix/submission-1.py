class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        lr = 0
        lc = 0
        rr = rows-1
        rc = cols-1

        res = []
        visit = set()
        while lr <= rr and lc <= rc:
            for i in range(lc, rc+1):
                if (lr, i) not in visit:
                    res.append(matrix[lr][i])
                visit.add((lr, i))
            lr+=1
            for i in range(lr, rr+1):
                if (i, rc) not in visit:
                    res.append(matrix[i][rc])
                visit.add((i, rc))
            
            rc-=1
            for i in range(rc, lc-1, -1):
                if (rr, i) not in visit:
                    res.append(matrix[rr][i])
                visit.add((rr, i))
            rr-=1
            for i in range(rr, lr-1, -1):
                if (i, lc) not in visit:
                    res.append(matrix[i][lc])
                visit.add((i, lc))
            lc+=1
        
        return res
