class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols):
                return False
            if board[r][c] == 'X' or (r,c) in visit:
                return True
            visit.add((r,c))
            res = dfs(r+1, c) and dfs(r-1, c) and dfs(r, c+1) and dfs(r, c-1)
            visit.remove((r,c))
            return res

        for r in range( rows-1):
            for c in range( cols):
                if board[r][c] == 'O':
                    if dfs(r, c):
                        board[r][c] = 'X'
        
        