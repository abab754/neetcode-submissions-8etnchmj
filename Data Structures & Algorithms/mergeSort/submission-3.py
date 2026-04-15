# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.divide(pairs, 0, len(pairs)-1)
    
    def divide(self, pairs, l, r):
        if l < r:
            m = (l+r)//2
            self.divide(pairs, l, m)
            self.divide(pairs, m+1, r)
            self.sort(pairs, l, m, r)
        return pairs
    
    def sort(self, pairs, l, m, r):
        idx1 = l
        idx2 = m+1
        idx3 = 0
        arr = [0] * (r-l+1)
        while idx1 <= m and idx2 <= r:
            if pairs[idx1].key <= pairs[idx2].key:
                arr[idx3] = pairs[idx1]
                idx1+=1
            else:
                arr[idx3] = pairs[idx2]
                idx2+=1
            idx3+=1
        
        while idx1 <= m:
            arr[idx3] = pairs[idx1]
            idx1+=1
            idx3+=1

        while idx2 <= r:
            arr[idx3] = pairs[idx2]
            idx2+=1
            idx3+=1

        idx1= l
        while idx1 <= r:
            pairs[idx1] = arr[idx1-l]
            idx1+=1
        
