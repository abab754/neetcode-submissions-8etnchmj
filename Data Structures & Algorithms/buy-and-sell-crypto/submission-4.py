class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        res = 0
        while r < len(prices) and l < r:
            if prices[l] >= prices[r]:
                l = r
                r=l+1
            else:
                res = max(res, prices[r] - prices[l])
                r+=1
        return res
        
            