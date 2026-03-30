import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = collections.defaultdict(int)
    
        p = 0
        res = 0
        hm[0] = 1
        for i in range(len(nums)):
            p += nums[i]
            if p - k in hm:
                res+=hm[p-k]
            hm[p]+=1

        return res