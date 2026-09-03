class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1

        heap = []
        for key, v in hm.items():
            heapq.heappush(heap, (-v, key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
            
