class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2):
                return False
            
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False
            
            j = len(s2)-1
            for i in range(len(s1)-1, -1, -1):
                if s1[i] != s2[j]:
                    return False
                j-=1
            
            return True
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res+=1
        
        return res