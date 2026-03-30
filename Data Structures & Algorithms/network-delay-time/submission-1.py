class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        
        heap = [(0, k)]
        visit = set()
        res= 0
        while heap:
            w, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            res= w

            for w1, n1 in adj[node]:
                if n1 not in visit:
                    heapq.heappush(heap, (w1+w, n1))
        
        if len(visit) == n:
            return res
        return -1