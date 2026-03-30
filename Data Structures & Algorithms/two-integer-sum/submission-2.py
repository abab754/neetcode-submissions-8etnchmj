class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in hm:
                res.append(hm[target - nums[i]])
                res.append(i)
                return res
            hm[nums[i]] = i
        return res
        