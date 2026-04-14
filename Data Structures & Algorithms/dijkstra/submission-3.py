import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        hm = defaultdict(list)
        for u, v, w in edges:
            hm[u].append((v, w))
        
        visit = set()
        res = {}
        for i in range(n):
            res[i] = -1

        heap = [(0, src)]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            visit.add(n1)
            res[n1] = w1
            for n2, w2 in hm[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w1+w2, n2))
        
        return res
