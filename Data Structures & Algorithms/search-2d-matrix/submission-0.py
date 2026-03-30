class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        r=0
        while r < rows:
            i = 0
            j = cols-1
            if matrix[r][i] > target:
                return False
            elif matrix[r][i] == target or matrix[r][j] == target:
                return True
            else:
                while i <= j:
                    m = int((i+j)/2)
                    if matrix[r][m] == target:
                        return True
                    elif matrix[r][m] > target:
                        j= m-1
                    else:
                        i = m+1
            r+=1

        return False
