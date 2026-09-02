class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        for i in s1:
            f1[ord(i) - 97] += 1

        for r in range(len(s2)):
            f2[ord(s2[r]) - 97] +=1
            if r >= len(s1):
                f2[ord(s2[r - len(s1)]) - 97] -=1
            if f1 == f2:
                return True

        return False
        