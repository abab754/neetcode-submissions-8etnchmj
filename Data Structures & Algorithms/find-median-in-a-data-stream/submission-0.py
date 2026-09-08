class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.left, -1 * num)
        elif len(self.left) == len(self.right):
            if num <= self.right[0]:
                heapq.heappush(self.left, -1 * num)
            else:
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))
                heapq.heappush(self.right, num)

        elif len(self.left) - len(self.right) > 0:
            if num >= -1 * self.left[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.right, -1 * heapq.heappop(self.left))
                heapq.heappush(self.left, -1 * num)
        elif len(self.right) - len(self.left) > 0:
            if num <= self.right[0]:
                heapq.heappush(self.left, -1 * num)
            else:
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))
                heapq.heappush(self.left, -1 * num)

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return ((-1 * self.left[0]) + self.right[0]) / 2
        else:
            return -1 * self.left[0]        