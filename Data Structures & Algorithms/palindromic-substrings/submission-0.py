class Solution:
    def countSubstrings(self, s: str) -> int:
        def f(i, j):
            if i <0 or j >= len(s) or s[i] != s[j]:
                return 0
            if s[i] == s[j]:
                return 1 + f(i-1, j+1)
        
        res = 0
        for i in range(len(s)):
            res += f(i, i) + f(i, i+1)
        return res