class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)
        for c in s:
            hm1[c] += 1
        
        for c in t:
            hm2[c] += 1
        
        return hm1 == hm2
