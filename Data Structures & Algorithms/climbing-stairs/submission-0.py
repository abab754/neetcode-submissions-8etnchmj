class Solution:
    def __init__(self):
        self.hm = {}
    def climbStairs(self, n):
        res = 0
        def dfs(i):
            if i in self.hm:
                return self.hm[i]
            if i >= n :
                self.hm[i] = (i == n)
                return i == n
            if i < n:
                return dfs(i+1) + dfs(i+2)

        return dfs(0)