class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            m = (l+r) //2
            day = 1
            i = 0
            curWeight = 0
            while i < len(weights) and day <= days:
                
                if weights[i] + curWeight > m:
                    day+=1
                    curWeight = weights[i]
                else:
                    curWeight += weights[i]
                i+=1
            if day > days:
                l = m+1
            else:
                res = min(res, m)
                r = m - 1
        
        return res