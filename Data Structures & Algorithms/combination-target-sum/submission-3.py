class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dp = {}
        res = []
        def dfs(i, cur, a):
            if a == target and cur not in res:
                res.append(cur[:])
                return
            
            if i>=len(nums) or a > target:
                return
            
            a+=nums[i]
            cur.append(nums[i])
            dfs(i, cur, a)
            a-=nums[i]
            cur.pop()
            dfs(i+1, cur, a)
        
        dfs(0, [], 0)
        return res