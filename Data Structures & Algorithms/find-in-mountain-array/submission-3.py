class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def peak(l, r):
            while l <= r:
                m = (l+r)//2
                if mountainArr.get(m-1) < mountainArr.get(m) > mountainArr.get(m+1):
                    return m
                elif mountainArr.get(m-1) < mountainArr.get(m) < mountainArr.get(m+1):
                    l = m
                else:
                    r= m
        
        def search(l, r):
            while l <= r:
                m = (l+r)//2
                mid = mountainArr.get(m)
                if mid == target:
                    return m
                elif mid > target:
                    r = m-1
                else:
                    l = m+1
            return float("inf")

        def search2(l, r):
            while l <= r:
                m = (l+r)//2
                mid = mountainArr.get(m)
                if mid == target:
                    return m
                elif mid < target:
                    r = m-1
                else:
                    l = m+1
            return float("inf")
        
        l = 0
        r = mountainArr.length()-1
        p = peak(l, r)
        res = min(search(l, p), search2(p, r))
        return res if res < float("inf") else -1
