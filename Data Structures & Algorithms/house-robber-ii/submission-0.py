class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        left = [0 for i in range(len(nums))]
        left[0] = nums[0]
        left[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            left[i] = max(nums[i]+left[i-2], left[i-1])


        right = [0 for i in range(len(nums))]
        right[-1] = nums[-1]
        right[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, 0, -1):
            right[i] = max(nums[i] + right[i+2], right[i+1])

        l = max(left)
        r = max(right)
        return max(l, r)