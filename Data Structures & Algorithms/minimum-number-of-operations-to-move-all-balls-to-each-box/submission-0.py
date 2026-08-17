class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        hm = {}
        for i in range(len(boxes)):
            if boxes[i] == '1':
                hm[i] = 1
        
        for i in range(len(boxes)):
            cur = 0
            for (key, val) in hm.items():
                cur += abs(key - i)
            res[i] = cur
        
        return res