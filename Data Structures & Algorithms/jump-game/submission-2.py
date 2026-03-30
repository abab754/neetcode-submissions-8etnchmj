class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[-1] = True
        target = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= target:
                dp[i] = True
                target = i
                continue
            if dp[nums[i] + i]:
                dp[i] = True
        
        return dp[0]
