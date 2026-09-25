class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0
        finished = 0
        heap = []
        q = deque()
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))
        
        while finished < len(tasks):
            cycle+=1
            while q and cycle - q[0][2] > n:
                popq = q.popleft()
                heapq.heappush(heap, (-popq[0], popq[1]))
            if not heap:
                cycle = q[0][2] + n
                continue
            count, task = heapq.heappop(heap)
            count = -count

            if count - 1 > 0:
                q.append([count-1, task, cycle])
            finished+=1            
        return cycle