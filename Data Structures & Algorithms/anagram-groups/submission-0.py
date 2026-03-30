class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str in hm:
                ls = hm.get(sorted_str)
                ls.append(s)
                hm[sorted_str] = ls
            else:
                hm[sorted_str] = [s]
        
        return list(hm.values())