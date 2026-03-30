class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[l] <= nums[m] <= nums[r]:
                res = min(nums[l], res)
                break
            elif nums[m] >= nums[l]:
                l= m+1
            elif nums[m] <= nums[l] and nums[m] <= nums[r]:
                res = min(nums[m], res)
                r = m - 1
            else:
                r = m - 1
        return res
        