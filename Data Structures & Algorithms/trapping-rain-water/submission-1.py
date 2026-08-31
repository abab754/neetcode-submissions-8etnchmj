class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        cur = height[0]
        for i in range(1, len(height)):
            maxL[i] = max(cur, height[i])
            cur = max(cur, height[i])
        
        cur = height[-1]
        for i in range(len(height)-2, -1, -1):
            maxR[i] = max(cur, height[i])
            cur = max(cur, height[i])
        
        res = 0
        for i in range(len(height)):
            if min(maxL[i], maxR[i]) - height[i] > 0:
                res += min(maxL[i], maxR[i]) - height[i]

        return res