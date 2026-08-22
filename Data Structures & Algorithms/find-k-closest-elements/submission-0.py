class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1

        while l <=r and r-l+1 >= k:
            if r-l+1 == k:
                return arr[l:r+1]
            if abs(arr[l]- x) > abs(arr[r] - x):
                l+=1
            else:
                r-=1
        
        