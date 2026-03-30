import collections
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append([w, v])
            adj[v].append([w, u])
        
        if len(adj.keys()) != n:
            return -1

        heap = [(0, 0, 0)]
        visit = set()
        cost = 0
        while len(visit) < n:
            if not heap:
                return -1
            weight, src, dest = heapq.heappop(heap)
            if dest in visit:
                continue
            visit.add(dest)
            cost+=weight
            for w1, d2 in adj[dest]:
                if d2 not in visit:
                    heapq.heappush(heap, (w1, src, d2))
        return cost
        