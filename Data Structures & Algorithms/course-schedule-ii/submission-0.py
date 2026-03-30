import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        res = []
        visit = set()
        def dfs(course):
            if course not in adj:
                if course not in res:
                    res.append(course)
                return True
            if adj[course] == []:
                if course not in res:
                    res.append(course)
                return True
            if course in visit:
                return False
            visit.add(course)
            for crs in adj[course]:
                if not dfs(crs):
                    return False
            visit.remove(course)
            adj[course] = []
            res.append(course)
            return True
            
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res