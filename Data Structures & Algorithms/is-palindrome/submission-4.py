class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        def back(l, r):
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return back(l+1,r-1)
            

        return back(0,len(s)-1)