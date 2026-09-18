class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[l] == target or nums[m] == target or nums[r] == target:
                return True
            if nums[m] == nums[l] == nums[r]:
                l+=1
                r-=1
            elif nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m+1 
                else:
                    r = m-1
            else:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m+1
        return False