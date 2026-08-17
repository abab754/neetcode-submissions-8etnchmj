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

    def longest(self):
        res = ""
        cur = self.root
        while True:
            if len(cur.children) != 1 or cur.end:
                return res
            c = next(iter(cur.children))
            res+=c
            cur = cur.children[c]
            if not cur.children:
                return res
        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.add(s)
        return trie.longest()


