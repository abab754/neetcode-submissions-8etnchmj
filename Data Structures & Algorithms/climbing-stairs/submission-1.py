class Solution:
    def climbStairs(self, n):
        res = 0
        def dfs(i):
            if i > n :
                return 0
            if i == n:
                return 1
            if i < n:
                return dfs(i+1) + dfs(i+2)

        return dfs(0)