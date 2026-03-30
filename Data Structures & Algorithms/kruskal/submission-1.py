import heapq
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]

    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.isSame(x, y):
            return False
        px = self.find(x)
        py = self.find(y)
        if self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        return True
        
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        for n1, n2, w in edges:
            heapq.heappush(heap, (w, n1, n2))

        i = 0
        uf = UnionFind(n)
        mst = 0
        while i < n-1:
            if not heap:
                return -1
            w, n1, n2 = heapq.heappop(heap)
            b = uf.union(n1, n2)
            if not b:
                continue
            i+=1
            mst+=w

        return mst