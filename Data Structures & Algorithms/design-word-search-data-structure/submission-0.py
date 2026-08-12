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

    def search(self, word, root):
        cur = root
        for i in range(len(word)):
            if word[i] == ".":
                for child in cur.children.values():
                    if i + 1 >= len(word):
                        return child.end
                    if self.search(word[i+1:], child):
                        return True
                return False
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.end

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word, self.trie.root)
        
