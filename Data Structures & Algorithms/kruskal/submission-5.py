import heapq

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * (n)
        self.parent = [i for i in range(n)]

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
        if self.isSame(x, y):
            return False
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.rank[px] += self.rank[py]
            self.parent[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.parent[px] = py
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        uf = UnionFind(n)
        for u, v, w in edges:
            heapq.heappush(heap, (w, u, v))
        res = 0
        comps = n
        while heap and comps > 1:
            w1, s1, d1 = heapq.heappop(heap)
            if uf.union(s1, d1):
                res+=w1
                comps-=1
        return res if comps == 1 else -1
        