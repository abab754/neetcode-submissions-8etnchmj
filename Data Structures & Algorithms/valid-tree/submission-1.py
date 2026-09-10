class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for edge in edges:
           
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            print(adj)
        
        visit = set()
        def dfs(cur, par):
            if cur in visit and par in visit:
                return False
            visit.add(cur)
            for nei in adj[cur]:
                if nei == par:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n