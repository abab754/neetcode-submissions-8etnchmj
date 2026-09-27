class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = (l+r)//2
            curSum = 0
            groups = 1

            for i in range(len(nums)):
                if curSum + nums[i] > m:
                    curSum = 0
                    groups+=1
                curSum+=nums[i]
            
            if groups <= k:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        
        return res