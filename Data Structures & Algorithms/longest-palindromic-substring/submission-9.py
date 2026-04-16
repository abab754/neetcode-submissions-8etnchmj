class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]* (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 1
        resLen = 0
        resIdx = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    if j - i +1 >= resLen:
                        resIdx = i
                        resLen = j-i+1
        
        return s[resIdx: resIdx+resLen]