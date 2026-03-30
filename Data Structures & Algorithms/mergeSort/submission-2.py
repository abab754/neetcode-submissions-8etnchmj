# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.divide(pairs, 0, len(pairs)-1)
    
    def divide(self, pairs, s, e):
        if s < e:
            m = (s+e)//2
            self.divide(pairs, s, m)
            self.divide(pairs, m+1, e)
            self.sort(pairs, s, m, e)
        return pairs
    
    def sort(self, nums, s, m, e):
        l = s
        r = m+1
        new_arr = [0 for i in range(e-s+1)]
        i = 0
        while l <= m and r <= e:
            if nums[l].key <= nums[r].key:
                new_arr[i] = nums[l]
                l+=1
            else:
                new_arr[i] = nums[r]
                r+=1
            i+=1
        
        while l <= m:
            new_arr[i] = nums[l]
            l+=1
            i+=1
        
        while r <= e:
            new_arr[i] = nums[r]
            r+=1
            i+=1
        
        l = s
        while l <= e:
            nums[l] = new_arr[l-s]
            l+=1
