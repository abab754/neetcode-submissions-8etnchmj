import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)
        while l <= r:
            k = int((l+r)/2)
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            if time <= h:
                res = min(k, res)
                r = k -1
            else:
                l = k+1
        
        return res

