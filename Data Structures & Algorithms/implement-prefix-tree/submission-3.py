class Node:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

    def index(self, char):
        return ord(char) - ord('a')

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        if self.search(word):
            return

        cur = self.root
        for c in word:
            idx = cur.index(c)
            if not cur.children[idx]:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = cur.index(c)
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = cur.index(c)
            if not cur.children[idx]:
                return False  
            cur = cur.children[idx]
        return True
        
        