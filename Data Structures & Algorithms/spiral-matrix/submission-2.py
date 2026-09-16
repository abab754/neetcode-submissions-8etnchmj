class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        lr = 0
        lc = 0
        rr = rows-1
        rc = cols-1

        res = []
        while lr <= rr and lc <= rc:
            for i in range(lc, rc+1):
                res.append(matrix[lr][i])
            lr+=1
            for i in range(lr, rr+1):
                res.append(matrix[i][rc])
            
            rc-=1
            if lr > rr or lc > rc:
                break

            for i in range(rc, lc-1, -1):
                res.append(matrix[rr][i])
            rr-=1
            for i in range(rr, lr-1, -1):
                res.append(matrix[i][lc])
            lc+=1
        
        return res
