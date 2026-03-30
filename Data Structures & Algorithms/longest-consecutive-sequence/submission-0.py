class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in s:
                cur = 0
                while num in s:
                    cur+=1
                    num+=1
                longest = max(longest, cur)
        return longest