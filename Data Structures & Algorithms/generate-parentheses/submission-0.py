class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o, c, s):
            if o == c == n:
                res.append(s)
            if o < n:
                s+='('
                backtrack(o+1, c, s)
                s = s[0:len(s)-1]
            if c < o:
                s+=')'
                backtrack(o, c+1, s)
                s = s[0:len(s)-1]
            
        backtrack(0, 0, '')
        return res