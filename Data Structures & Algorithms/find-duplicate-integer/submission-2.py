class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while f < len(nums):
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while s < len(nums):
            if s == s2:
                return s
            s = nums[s]
            s2 = nums[s2]        