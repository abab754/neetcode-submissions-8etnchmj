class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        res = []
        
        for s in strs:
            sorted_s = str(sorted(s))
            hm[sorted_s].append(s)
        
        for v in hm.values():
            res.append(v)

        return res