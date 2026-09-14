class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = heights[0]
        for i in range(len(heights)):
            ind = -1
            while stack and heights[i] < stack[-1][0]:
                res = max(res, (stack[-1][0]) * (i - stack[-1][1]))
                num, ind = stack.pop()
            if ind >= 0:
                stack.append((heights[i], ind))
            else:
                stack.append((heights[i], i))
        
        while stack:
            res = max(res, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()
            
            
        return res