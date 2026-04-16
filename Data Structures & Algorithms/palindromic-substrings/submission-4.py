class Solution:
    def countSubstrings(self, s: str) -> int:
        def dfs(i, j):
            if i < 0 or j >= len(s):
                return 0
            if s[i]!= s[j]:
                return 0
            return 1 + dfs(i-1, j+1)
        res = 0
        for i in range(len(s)):
            res += dfs(i, i) + dfs(i, i+1)

        return res
