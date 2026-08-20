class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        hm = defaultdict(list)
        for p, c in prerequisites:
            hm[p].append(c)

        visit = set()
        def dfs(course):
            if course not in hm:
                return True
            if course in visit:
                return False
            visit.add(course)
            for crs in hm[course]:
                if not dfs(crs):
                    return False
            hm[course] = []
            visit.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True