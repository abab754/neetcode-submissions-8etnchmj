class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ct = 1
        hm = {}
        inc = False
        for i in range(1, numRows+1):
            hm[i] = ""
        
        for i in range(len(s)):
            hm[ct]+=s[i]
            if ct == numRows or ct == 1:
                inc = not inc
            if inc:
                ct+=1
            else:
                ct-=1
        res = "" 
        for i in range(1, numRows+1):
            res += hm[i]
        
        return res