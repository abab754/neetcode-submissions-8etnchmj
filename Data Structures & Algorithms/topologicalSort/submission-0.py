class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        res = []
        visited = set()
        visiting = set()

        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False

            visiting.add(src)
            for dst in adj[src]:
                if not dfs(dst):
                    return False

            visiting.remove(src)
            visited.add(src)
            res.append(src)
            return True

        for i in range(n):
            if not dfs(i):
                return []
            
        res.reverse()
        return res