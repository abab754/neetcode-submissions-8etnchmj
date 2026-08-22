class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        res = float("inf")
        total = 0
        while i <= j and j < len(nums):
            if total + nums[j] >= target:
                res = min(res, j-i+1)
                total -= nums[i]
                i+=1
                continue
            total+=nums[j]
            j+=1

        if res == float("inf"):
            return 0
        return res