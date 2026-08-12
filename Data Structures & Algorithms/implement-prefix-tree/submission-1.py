class Node:
    def __init__(self):
        self.end = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        if self.search(word):
            return

        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = Node()
            cur = cur.children[word[i]]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]   
        return True
        
        