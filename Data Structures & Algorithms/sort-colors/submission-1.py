class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = 0
                l+=1
        
        for i in range(l, len(nums)):
            if nums[i] == 1:
                nums[i] = nums[l]
                nums[l] = 1
                l+=1
        
        
 

        