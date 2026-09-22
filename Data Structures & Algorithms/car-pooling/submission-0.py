class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        numPass = 0
        trips.sort(key=lambda x:x[1])

        for trip in trips:
            while heap and trip[1] >= heap[0][0]:
                pop_trip = heapq.heappop(heap)
                numPass -= pop_trip[1]
            numPass+=trip[0]
            heapq.heappush(heap, (trip[2], trip[0], trip[1]))
            if numPass > capacity:
                return False
        
        return True