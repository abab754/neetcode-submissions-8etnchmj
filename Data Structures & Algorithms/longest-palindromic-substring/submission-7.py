class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n+1)] for j in range(n+1)]
        resLen = 0
        resInd = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > resLen:
                        resLen = j-i+1
                        resInd = i
        
        return s[resInd: resInd+resLen]
                