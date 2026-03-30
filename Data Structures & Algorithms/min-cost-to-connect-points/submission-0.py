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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        uf = UnionFind(len(points))
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1 , len(points)):
                x2, y2 = points[j]
                w = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(heap, (w, i , j))

        i = 0
        mst = 0
        while i < len(points) - 1:
            if not heap:
                return -1
            w, p1, p2 = heapq.heappop(heap)
            if not uf.union(p1, p2):
                continue
            i+=1
            mst += w
        return mst
        