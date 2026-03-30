class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [float("inf") for i in range(n)]
        arr[src] = 0
        for i in range(k+1):
            tmp = arr[:]
            for f, t, p in flights:
                tmp[t] = min(arr[f]+p, tmp[t])
            arr = tmp
        return -1 if arr[dst] == float("inf") else arr[dst]