class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return
        k = k % len(nums)
        
        l = 0
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l+=1
            r-=1
        
        l = 0
        r = k - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l+=1
            r-=1
        
        l = k
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l+=1
            r-=1
        