class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        side = total//2
        # dp = {}
        sides = [0] * 2
        nums.sort(reverse=True)
        def dfs(i):
            if i >= len(nums):
                return True
            # if set(sorted(sides)) in dp:
            #     return dp[set(sorted(sides))]
            for j in range(2):
                if sides[j] + nums[i] > side:
                    continue
                sides[j] += nums[i]
                if dfs(i+1):
                    return True
                sides[j] -= nums[i]
            
            return False

        return dfs(0)
