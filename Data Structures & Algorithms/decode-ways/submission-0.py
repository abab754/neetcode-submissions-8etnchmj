class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1

        hm = {str(i): i for i in range(1, 27)}

        for i in range(n-1, -1, -1):
            if s[i] == 0:
                dp[i] = 0
                continue
            if i + 1 >= n:
                dp[i] = dp[i+1] if s[i] in hm else 0
                continue
            b1 = s[i] in hm
            b2 = s[i:i+2] in hm
            if b1 and b2:
                dp[i] = dp[i+1] + dp[i+2]
            elif not b1 and not b2:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        return dp[0]