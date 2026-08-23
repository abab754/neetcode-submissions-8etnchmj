class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)

        for c in t:
            hm2[c]+=1

        have = 0
        need = len(hm2)

        l = 0
        minLen = float("inf")
        res = ""
        for r in range(len(s)):
            hm1[s[r]]+=1
            if s[r] in hm2 and hm1[s[r]] == hm2[s[r]]:
                have+=1

            # if b:
            #     if r-l+1 < minLen:
            #         minLen = r-l+1
            #         res = s[l:r+1]
            while l<=r and have == need:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    res = s[l:r+1]
                
                hm1[s[l]]-=1
                if hm1[s[l]] < hm2[s[l]]:
                    have -= 1
                l+=1
            
        return res

