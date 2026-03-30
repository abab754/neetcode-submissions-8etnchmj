class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(m)] for j in range(n)]
        def f(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + f(i+1, j+1)
                return dp[i][j]
            dp[i][j] = max(f(i+1, j), f(i, j+1))
            return dp[i][j] 
        
        return f(0, 0)