class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        res = ""
        q = deque()
        freq = defaultdict(int)

        for c in s:
            freq[c]+=1
        
        for c, count in freq.items():
            if count >= len(s) -1 and len(s) > 2:
                return ""
            heapq.heappush(heap, (-count, c))
        
        while heap:
            pop = heapq.heappop(heap)
            res+=pop[1]
            if -pop[0] - 1 > 0:
                q.append([-pop[0]-1, pop[1]])
            if q and q[0][1] != res[-1]:
                popq = q.popleft()
                heapq.heappush(heap, (-popq[0], popq[1]))
        
        return "" if len(q) > 0 else res
