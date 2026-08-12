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
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                cur.children[word[i]] = Node()
                cur = cur.children[word[i]]
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                return False
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] in cur.children:
                cur = cur.children[prefix[i]]
            else:
                return False
        return True
        
        