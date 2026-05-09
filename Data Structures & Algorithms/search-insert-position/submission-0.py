class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                if m+1 == len(nums):
                    return m+1
                if nums[m+1] > target:
                    return m+1
                l = m+1
            else:
                if m == 0:
                    return 0
                if nums[m-1] < target:
                    return m
                r = m - 1
        
