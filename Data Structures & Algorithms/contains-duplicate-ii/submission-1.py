class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visit = set()
        l = 0
        for i in range(len(nums)):
            if i > k:
                visit.remove(nums[l])
                l+=1
            if nums[i] in visit:
                return True
            visit.add(nums[i])
        return False