import collections
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))
        
        heap = [(0,0)]
        visit = set()
        mst=0

        while len(visit) < n:

            if not heap:
                return -1
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            visit.add(n1)
            mst+=w1
            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w2, n2))

        return mst

        