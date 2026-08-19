class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = 0
        r = int(x/2)
        res = -1
        while l <= r:
            m = (l+r)//2
            if m*m > x:
                r = m-1
            elif m*m == x:
                return m
            else:
                res = max(res, m)
                l= m+1
        return res