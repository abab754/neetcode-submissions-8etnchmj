class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        res = ""
        cur = ""
        if len(strs[0]) < 1:
            return res
        if len(strs) < 2:
            return strs[0]
        for i in range(len(strs[0])):
            cur += strs[0][i]
            for j in range(1, len(strs)):
                if not strs[j].startswith(cur):
                    return res
            res = cur
        return res