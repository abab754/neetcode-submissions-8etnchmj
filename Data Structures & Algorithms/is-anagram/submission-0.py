class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}

        for c in s:
            hms[c] = hms.get(c, 0) + 1

        for c in t:
            hmt[c] = hmt.get(c, 0) + 1
        
        return hms == hmt