class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        r = len(prices)-1
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > prices[r]:
                r=i
            else:
                res+=prices[r] - prices[i]
                r=i
        return res