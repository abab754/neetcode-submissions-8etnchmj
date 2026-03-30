class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [101]*len(nums)
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= len(nums)-1:
                dp[i] = 1
                goal = i
                continue
            if i + nums[i] >= goal:
                dp[i] = min(1 + dp[goal], 1+dp[i+nums[i]])
                goal = i
        
        return dp[0]