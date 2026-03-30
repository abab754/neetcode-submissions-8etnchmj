class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        curSum = 0
        for i in range(len(arr)):
            if i >= k:
                if curSum/k >= threshold:
                    res+=1
                curSum-=arr[l]
                l+=1
            curSum+=arr[i]
        if curSum/k >= threshold:
            res+=1
        return res