class Solution:

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [[-1] * (capacity + 1) for _ in range(len(profit))]

        def dfs(i, cap, cash):
            if i == len(profit):
                return 0
            if cash[i][cap] != -1:
                return cash[i][cap]

            cash[i][cap] = dfs(i+1, cap, cash)

            new_cap = cap - weight[i]
            if new_cap >= 0:
                p2 = profit[i] + dfs(i+1, new_cap, cash)
                cash[i][cap] = max(cash[i][cap], p2)
            return cash[i][cap]

        return dfs(0, capacity, cache)