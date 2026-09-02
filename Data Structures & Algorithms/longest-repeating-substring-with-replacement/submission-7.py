class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        maxf = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord("A")] +=1
            maxf = max(maxf, freq[ord(s[r]) - ord("A")])
            if r-l+1 - maxf > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l+=1
            
        return len(s) - l