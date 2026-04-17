import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hm = defaultdict(list)
        heap = [(0, k)]
        for u, v, w in times:
            hm[u].append([v, w])
        
        visit = set()
        res = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            res = w1
            for n2, w2 in hm[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w2+w1, n2))
        
        if len(visit) != n:
            return -1
        return res
