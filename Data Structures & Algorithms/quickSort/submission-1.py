# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.divide(pairs, 0, len(pairs)-1)
        return pairs
    
    def divide(self, nums, s, e):
        if s < e:
            pid = e
            i = s
            j = i
            while i < pid:
                if nums[i].key < nums[pid].key:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    j+=1
                i+=1
            tmp = nums[j]
            nums[j] = nums[pid]
            nums[pid] = tmp
            self.divide(nums, s, j-1)
            self.divide(nums, j+1, e)
