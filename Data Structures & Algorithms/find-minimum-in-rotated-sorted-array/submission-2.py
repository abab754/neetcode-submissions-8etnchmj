class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            m = int((l+r)/2)
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m - 1
        return res
