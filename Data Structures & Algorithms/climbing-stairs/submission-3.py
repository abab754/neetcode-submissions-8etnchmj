class Solution:
    def climbStairs(self, n):
        p1 = 1
        p2 = 1
        for _ in range(n-1):
            tmp = p2
            p2 = p1+p2
            p1= tmp
        return p2
           