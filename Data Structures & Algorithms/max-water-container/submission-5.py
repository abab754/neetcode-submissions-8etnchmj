class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            cur = (min(heights[l], heights[r]) * (r-l))
            if cur > res:
                res = cur
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return res
