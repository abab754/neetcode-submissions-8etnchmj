class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s)) + '!' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        lens = ''
        while i < len(s):
            if s[i] == '!':
                str_len = int(lens)
                res.append(s[i+1:i+1+str_len])
                i = i+1+str_len
                lens = ''
            else:
                lens += s[i]
                i+=1
        return res
