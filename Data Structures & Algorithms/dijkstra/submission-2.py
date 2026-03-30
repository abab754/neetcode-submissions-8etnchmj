import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        heap = [(0, src)]
        shortest = {}
        adj = {}
        for i in range(n):
            adj[i] = []

        for u,v,w in edges:
            adj[u].append([w,v])
        
        while heap:
            w1, n1 = heapq.heappop(heap)
            print(n1,w1)
            if n1 in shortest:
                continue
                
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                heapq.heappush(heap, (w1+w2, n2))
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest