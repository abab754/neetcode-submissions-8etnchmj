import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            distance = math.sqrt(((point[0] - 0)**2) + ((point[1] - 0) **2))
            tup = (distance, point)
            heapq.heappush(heap, tup)
        
        for _ in range(k):
            if len(heap) >0:
                tup = heapq.heappop(heap)
                res.append(tup[1])
            else:
                break
        
        return res

