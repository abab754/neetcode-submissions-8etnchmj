class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        side = sum(nums) // k
        sides = [0] * k
        nums.sort(reverse=True)
        def dfs(i, cur):
            if i >= len(nums):
                return True
            
            for j in range(k):
                if cur[j] + nums[i] > side:
                    continue
                cur[j] += nums[i]
                if dfs(i+1, cur):
                    return True
                cur[j] -= nums[i]
                if cur[j] == 0:
                    break
            return False
        
        return dfs(0, sides)
