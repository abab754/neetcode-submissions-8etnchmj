import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1*num)
        
        res = 0
        for i in range(k):
            res = -1 * heapq.heappop(heap)
        return res