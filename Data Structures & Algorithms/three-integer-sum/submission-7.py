class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i-1]:
                i+=1
            l = i+1
            r = len(nums) -1
            while l < r:
                
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0:
                    cur = [nums[i], nums[l], nums[r]]
                    if cur not in res:
                        res.append(cur)
                    l += 1
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    r-=1
            i += 1
            
        return res