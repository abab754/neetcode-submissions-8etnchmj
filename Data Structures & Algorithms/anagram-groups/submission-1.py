class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        res = []
        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str in hm:
                val = hm.get(sorted_str)
                val.append(s)
                hm[sorted_str] = val
            else:
                hm[sorted_str] = [s]
        for v in hm.values():
            res.append(v)
        return res