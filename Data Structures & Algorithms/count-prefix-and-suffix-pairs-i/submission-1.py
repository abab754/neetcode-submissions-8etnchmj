class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

# class Trie:
#     def __init__(self):
#         self.root = Node()
    
#     def add(self, word):
#         i = 0
#         j = len(word)-1
#         cur = self.root
#         while i < len(word) and j >= 0:
#             tup = (word[i], word[j])
#             if tup not in cur.children:
#                 cur.children[tup] = Node()
#             cur = cur.children[tup]
#         cur.end = True


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = Node()
        res = 0
        for i in range(len(words)-1, -1, -1):
            word = words[i]
            l = 0
            r = len(word)-1
            cur = root
            while l < len(word) and r >= 0:
                tup = (word[l], word[r])
                if tup not in cur.children:
                    cur.children[tup] = Node()
                cur = cur.children[tup]
                cur.count+=1
                l+=1
                r-=1
            res += (cur.count - 1)
        return res
