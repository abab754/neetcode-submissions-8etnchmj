class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [float("inf")] * (len(s)+1)
        dp[-1] = 0
        
        for i in range(len(s)-1, -1, -1):
            for word in dictionary:
                if i + len(word) > len(s):
                    dp[i] = min(dp[i], dp[i+1]+1)
                    continue
                if s[i:i+len(word)] in dictionary:
                    dp[i] = min(dp[i], dp[i+len(word)])
            dp[i] = min(dp[i], dp[i+1]+1)

        return dp[0]