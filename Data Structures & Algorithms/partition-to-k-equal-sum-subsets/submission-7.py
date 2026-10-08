class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        side = sum(nums) // k
        sides = [0] * k
        nums.sort(reverse=True)
        def dfs(i):
            if i >= len(nums):
                return True
            
            for j in range(k):
                if sides[j] + nums[i] > side:
                    continue
                sides[j] += nums[i]
                if dfs(i+1):
                    return True
                sides[j] -= nums[i]
                if sides[j] == 0:
                    break
            return False
        
        return dfs(0)