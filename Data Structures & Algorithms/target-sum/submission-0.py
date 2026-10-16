class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, a):
            if i >= len(nums):
                if a == target:
                    dp[(i, a)] = 1
                else:
                    dp[(i,a)] = 0
                return dp[(i,a)]
            if (i, a) in dp:
                return dp[(i, a)]
            sub = dfs(i+1, a-nums[i])
            add = dfs(i+1, a+nums[i])
            dp[(i, a)] = sub + add
            return dp[(i, a)]

        return dfs(0, 0)