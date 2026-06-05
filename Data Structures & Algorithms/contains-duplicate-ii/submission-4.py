class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        visit = set()
        for i in range(len(nums)):
            if nums[i] in visit:
                return True
            visit.add(nums[i])
            if i >= k:
                visit.remove(nums[i-k])
            
        return False

            