class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(set)
        for c, p in prerequisites:
            hm[c].add(p)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if crs not in hm or len(hm[crs]) == 0:
                return True
            visit.add(crs)
            for c in hm[crs]:
                if not dfs(c):
                    return False
            hm[crs] = set()
            visit.remove(crs)
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
            visit = set()
        
        return True