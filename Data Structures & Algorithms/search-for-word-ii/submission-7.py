class Node:
    def __init__(self):
        self.end = False
        self.children = {}
        self.refs = 0
    
    def add(self, word):
        cur = self
        cur.refs+=1
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            cur.refs+=1
        cur.end = True

    def remove(self, word):
        cur = self
        cur.refs-=1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -=1 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = Node()
        for word in words:
            root.add(word)

        visit = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, node, cur):
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or board[r][c] not in node.children or node.children[board[r][c]].refs <= 0:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            cur += board[r][c]

            if node.end:
                node.end = False
                res.add(cur)
                root.remove(cur)
            
            dfs(r+1, c, node, cur)
            dfs(r-1, c, node, cur)
            dfs(r, c+1, node, cur)
            dfs(r, c-1, node, cur)
            visit.remove((r,c))  

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)