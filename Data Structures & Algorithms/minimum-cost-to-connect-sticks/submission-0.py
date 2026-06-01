import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total = 0
        while len(sticks) >= 2:
            i1 = heapq.heappop(sticks)
            i2 = heapq.heappop(sticks)
            a = i1+i2
            total+=a
            heapq.heappush(sticks, a)
        
        return total