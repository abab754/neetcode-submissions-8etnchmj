class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        i = 0
        while i < len(nums):
            if nums[i] in s:
                return nums[i]
            s.add(nums[i])
            i = nums[i]
        