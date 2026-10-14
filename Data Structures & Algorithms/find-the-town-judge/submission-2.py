class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hm = defaultdict(list)
        for a, b in trust:
            hm[b].append(a)
        visit = set()
        def dfs(i):
            if i not in hm:
                return True
            if i in visit:
                return False
            visit.add(i)
            for num in hm[i]:
                if not dfs(num):
                    return False
            visit.remove(i)
            return True

        def check(i):
            if i not in hm:
                return False
            for num in range(1, n+1):
                if num == i:
                    continue
                if num not in hm[i]:
                    return False
            return True

        for i in range(1, n+1):
            if i in hm and check(i) and dfs(i):
                return i
        return -1