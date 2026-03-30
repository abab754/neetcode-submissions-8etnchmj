class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r: 
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                break
            m = (l+r)//2
            if nums[m] <= nums[r]:
                res = min(res, nums[m])
                r = m-1
            else:
                l=m+1
        return res
        