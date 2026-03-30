class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        ret = []
        for i in range(len(nums)):
            if target - nums[i] in hm:
                ret = [hm.get(target-nums[i]), i]
                return ret
            hm[nums[i]] = i
        