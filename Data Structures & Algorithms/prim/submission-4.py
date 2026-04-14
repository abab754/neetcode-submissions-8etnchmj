import collections
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        hm = collections.defaultdict(list)
        for u, v, w in edges:
            hm[u].append((w, v))
            hm[v].append((w, u))
        
        visit = set()
        res = 0
        heapq.heappush(heap, (0, 0))

        while heap and len(visit) < n:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            res += w1
            visit.add(n1)
            for w2, n2 in hm[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w2, n2))
        return res if len(visit) == n else -1


        