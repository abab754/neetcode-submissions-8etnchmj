class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i, cap):
            if i == len(profit):
                return 0
            maxP = dfs(i+1, cap)
        
            new_cap = cap - weight[i]
            if new_cap >= 0:
                p = profit[i] + dfs(i+1, new_cap)
                maxP = max(maxP, p)
            return maxP

        return dfs(0, capacity)