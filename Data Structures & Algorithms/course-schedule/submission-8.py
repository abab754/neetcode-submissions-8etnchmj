class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()
        def dfs(course):
            if course not in adj:
                return True
            if course in visit:
                return False
            visit.add(course)
            for c in adj[course]:
                if not dfs(c):
                    return False
            visit.remove(course)
            adj[course] = []
            return True

        for co in range(numCourses):
            if not dfs(co):
                return False
            
        return True
                
