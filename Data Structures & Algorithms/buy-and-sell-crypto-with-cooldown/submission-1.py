class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices)+1)]
        def f(i, buy):
            if i >= len(prices):
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            profit = 0
            if buy:
                #option 1
                profit -= prices[i]
                profit += f(i+1, False)

                #option 2
                profit = max(profit, f(i+1, True))
                dp[i][buy] = profit
                return dp[i][buy]
            else:
                #option 1
                profit += prices[i]
                profit += f(i+2, True)

                profit = max(profit, f(i+1, False))
                dp[i][buy] = profit
                return dp[i][buy]
        
        return f(0, True)