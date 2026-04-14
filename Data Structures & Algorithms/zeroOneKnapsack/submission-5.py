class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[-1] * (M+1) for _ in range(N)]
        def dfs(i, cap, cache):
            if i >= len(profit):
                return 0
            if cache[i][cap] != -1:
                return cache[i][cap]
            # skip
            maxProfit = dfs(i+1, cap, cache)

            #take
            newCap = cap - weight[i]
            if newCap >=0:
                p = profit[i] + dfs(i+1, newCap, cache)
                maxProfit = max(maxProfit, p)
            cache[i][cap] = maxProfit
            return maxProfit

        return dfs(0, capacity, dp)

