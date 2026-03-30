import heapq
import collections
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append([succProb[i], edges[i][1]])
            adj[edges[i][1]].append([succProb[i], edges[i][0]])

        heap = [(-1, start_node)]
        visit = set()
        res = 0
        while end_node not in visit:
            if not heap:
                return 0
            prob, n = heapq.heappop(heap)
            prob *= -1
            res = prob
            if n in visit:
                continue
            visit.add(n)
            for prob1, n1 in adj[n]:
                if n1 not in visit:
                    heapq.heappush(heap, (prob1 * prob * -1, n1))

        return res if res > 0 else 0


