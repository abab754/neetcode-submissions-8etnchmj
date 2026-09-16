class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        lr = 0
        rr = rows-1
        while lr < rr:
            for c in range(cols):
                tmp = matrix[lr][c]
                matrix[lr][c] = matrix[rr][c]
                matrix[rr][c] = tmp
            lr+=1
            rr-=1
        
        for i in range(rows):
            for j in range(i+1, rows):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
