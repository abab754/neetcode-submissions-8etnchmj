class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        l = 0
        r = len(s) -1
        while l <=r:
            while r > 0 and not s[r].isalnum():
                r-=1
            while l < len(s) and not s[l].isalnum():
                l+=1
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True