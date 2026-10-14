class Solution:
    def __init__(self):
        self.reps = 0
    def validPalindrome(self, s: str) -> bool:

        def dfs(l, r):
            while l < r:
                if s[l] != s[r]:
                    if self.reps >= 1:
                        return False
                    self.reps+=1
                    return dfs(l+1, r) or dfs(l, r-1)
                else:
                    l+=1
                    r-=1
            return True
        return dfs(0, len(s)-1)