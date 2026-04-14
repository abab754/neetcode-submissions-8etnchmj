class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[-1] * (M+1) for _ in range(N)]
        def dfs(i, cap):
            if i >= N:
                return 0
            if dp[i][cap] != -1:
                return dp[i][cap]
            # skip
            maxProfit = dfs(i+1, cap)

            #take
            newCap = cap - weight[i]
            if newCap >=0:
                p = profit[i] + dfs(i+1, newCap)
                maxProfit = max(maxProfit, p)
            dp[i][cap] = maxProfit
            return maxProfit

        return dfs(0, capacity)

