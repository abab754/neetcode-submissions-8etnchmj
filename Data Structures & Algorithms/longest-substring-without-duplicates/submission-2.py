class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0] * 95
        l = 0
        res = 0
        for r in range(len(s)):
            while freq[ord(s[r]) - 95] > 0:
                freq[ord(s[l]) - 95] -= 1
                l+=1
            freq[ord(s[r]) - 95] += 1
            res = max(res, r-l+1)
        return res