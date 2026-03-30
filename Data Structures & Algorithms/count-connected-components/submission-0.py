class UnionFind:
    def __init__(self, n):
        self.parent = [i  for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]
        self.numComponents = n

    def find(self, x):
        px = self.parent[x]
        while px != self.parent[px]:
            px = self.parent[px]
        return px

    def isSame(self, x, y):
        px = self.find(x)
        py = self.find(y)
        return px == py
    
    def union(self, x, y):
        if self.isSame(x,y):
            return False
        px =self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        self.numComponents -= 1
        return True
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.numComponents
        