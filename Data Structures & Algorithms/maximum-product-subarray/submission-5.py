class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmax = 1
        cmin = 1

        for num in nums:
            tmp = cmax * num
            cmax = max(num, tmp, num*cmin)
            cmin = min(num, tmp, num*cmin)
            res = max(res, cmax)
        
        return res