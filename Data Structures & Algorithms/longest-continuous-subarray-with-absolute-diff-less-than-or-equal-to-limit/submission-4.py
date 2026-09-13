class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        res = 1
        minq = deque()
        maxq = deque()
        
        for r in range(len(nums)):
            while minq and nums[r] < minq[-1]:
                minq.pop()
            minq.append(nums[r])
            while maxq and nums[r] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[r])
            if abs(maxq[0] - minq[0]) <= limit:
                res = max(res, r-l+1)
            else:
                if maxq[0] == nums[l]:
                    maxq.popleft()
                if minq[0] == nums[l]:
                    minq.popleft()
                l+=1
        return res