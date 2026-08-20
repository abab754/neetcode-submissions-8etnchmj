import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        for c, p in prerequisites:
            hm[c].append(p)
        
        res = []
        visit = set()

        def dfs(course):
            if course not in hm:
                if course not in res:
                    res.append(course)
                return True
            if course in visit:
                return False
            visit.add(course)
            for crs in hm[course]:
                if not dfs(crs):
                    return False
            if course not in res:
                res.append(course)
            hm[course] = []
            visit.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res