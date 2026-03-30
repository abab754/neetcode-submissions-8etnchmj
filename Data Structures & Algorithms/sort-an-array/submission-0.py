class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        return nums
    def mergeSort(self,nums, l, r):
        if l < r:
            m = (l+r)//2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m+1, r)
            self.merge(nums, l, m, r)
    
    def merge(self, nums, l, m, r):
        extra = [0 for i in range(r-l+1)]
        i = l
        j = m+1
        k = 0
        while i <= m and j <= r:
            if nums[i] <= nums[j]:
                extra[k] = nums[i]
                i+=1
            else:
                extra[k] = nums[j]
                j+=1
            k+=1
        while i <= m:
            extra[k] = nums[i]
            i+=1
            k+=1
        while j <= r:
            extra[k] = nums[j]
            j+=1
            k+=1

        i = l 
        while i <= r:
            nums[i] = extra[i-l]
            i+=1
        