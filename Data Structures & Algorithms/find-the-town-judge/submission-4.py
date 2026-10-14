class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hm = defaultdict(set)
        for a, b in trust:
            hm[a].add(b)

        def check(i):
            for num in range(1, n+1):
                if num == i:
                    continue
                if i not in hm[num]:
                    return False
            return True

        for i in range(1, n+1):
            if i not in hm and check(i):
                return i
        return -1