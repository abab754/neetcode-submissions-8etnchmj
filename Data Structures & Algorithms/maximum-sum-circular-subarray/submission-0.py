class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        gmax = nums[0]
        gmin = nums[0]
        cmax = 0
        cmin = 0
        for i in nums:
            cmax = max(i, i + cmax)
            cmin = min(i, i + cmin)
            gmax = max(gmax, cmax)
            gmin = min(gmin, cmin)
            total += i
        if gmax < 0:
            return gmax
        return max(gmax,total - gmin)
