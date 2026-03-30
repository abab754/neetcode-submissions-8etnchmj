class Solution:
    def climbStairs(self, n):
        one = 1
        two = 1
        for i in range(n-1):
            tmp = one
            one = one+two
            two = tmp
        return one