class UnionFind:
    def __init__(self, n):
        self.rank = [1 for i in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def getRoot(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def isSame(self, x, y):
        px = self.getRoot(x)
        py = self.getRoot(y)
        return px == py
    
    def union(self, x, y):
        if self.isSame(x, y):
            return False
        px = self.getRoot(x)
        py = self.getRoot(y)
        if self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for i in range(len(edges)):
            src = edges[i][0]
            dest = edges[i][1]
            b = uf.union(src, dest)
            if not b:
                return edges[i]


        

