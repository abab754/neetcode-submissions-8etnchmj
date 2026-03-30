class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i+len(nums)] = nums[i]
        return arr