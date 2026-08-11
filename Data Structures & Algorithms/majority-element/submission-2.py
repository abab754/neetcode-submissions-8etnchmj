class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] = hm[num] + 1
        return max(hm, key=hm.get)