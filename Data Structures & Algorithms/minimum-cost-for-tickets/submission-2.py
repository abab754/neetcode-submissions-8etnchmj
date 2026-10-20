class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        trip = [1, 7, 30]
        dp = [0] * (len(days) + 1)
        for i in range(len(days)-1, -1, -1):
            best = float("inf")
            for t in range(3):
                j = i
                while j < len(days) and days[j] < days[i] + trip[t]:
                    j+=1
                best = min(best, costs[t] + dp[j])
            dp[i] = best

        return dp[0]