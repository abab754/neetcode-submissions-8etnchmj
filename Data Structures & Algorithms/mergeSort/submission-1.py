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
        return pairs
    
    def sort(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i = 0
        j = 0
        k = s
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    
        
