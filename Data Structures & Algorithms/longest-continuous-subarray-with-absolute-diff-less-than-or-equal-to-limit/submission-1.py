class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = float("-inf")
        l = 0
        gmax = nums[0]
        gmin = nums[0]
        for r in range(len(nums)):
            gmax = max(gmax, nums[r])
            gmin = min(gmin, nums[r])
            if abs(gmax - gmin) <= limit:
                res = max(res, r-l+1)
            else:
                l+=1
                gmax = max(nums[l:r+1])
                gmin = min(nums[l:r+1])
        
        return res