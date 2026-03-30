class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def f(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            f(i+1)
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            f(i+1)
        f(0)
        return res
            