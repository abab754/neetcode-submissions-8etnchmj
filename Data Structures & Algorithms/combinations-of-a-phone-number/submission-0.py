class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if not digits:
            return res
        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append("".join(cur[:]))
                return
            if i >= len(digits):
                return
            for c in map[digits[i]]:
                cur.append(c)
                dfs(i+1, cur)
                cur.pop()
        
        dfs(0, [])
        return res

