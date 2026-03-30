class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0] * 128
        l=0
        res = 0
        for r in range(len(s)):
            freq[ord(s[r]) - 128] += 1
            while l <= r and freq[ord(s[r]) - 128] > 1:
                freq[ord(s[l]) - 128] -= 1
                l+=1
            res = max(res, r-l + 1)
        
        return res