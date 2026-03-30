class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmax = nums[0]
        cmin = nums[0]
        gmax = nums[0]
        gmin = nums[0]
        total = sum(nums)

        for i in range(1, len(nums)):
            cmax = max(nums[i], nums[i] + cmax) 
            cmin = min(nums[i], nums[i] + cmin)
            gmax = max(cmax, gmax)
            gmin = min(gmin, cmin)
        if gmax <0:
            return gmax
        return max(total - gmin, gmax)
