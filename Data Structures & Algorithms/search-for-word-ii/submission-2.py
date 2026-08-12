class Node:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def prefix(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        trie = Trie()
        for word in words:
            trie.add(word)

        visit = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, cur):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit:
                return
            cur += board[r][c]
            if not trie.prefix(cur):
                return 
            if trie.search(cur):
                res.add(cur)
            visit.add((r,c))
            dfs(r+1, c, cur)
            dfs(r-1, c, cur)
            dfs(r, c+1, cur)
            dfs(r, c-1, cur)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "")
        
        return list(res)