class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def back(i, cur, tot):
            if  i >= len(nums) or tot > target :
                return
            if tot == target:
                res.append(cur[:])
                return
            else:
                cur.append(nums[i])
                back(i, cur, tot+nums[i])
                cur.pop()
                back(i+1, cur, tot)
                
        back(0, [], 0)
        return res
