class NumArray:

    def __init__(self, nums: List[int]):
        self.total = sum(nums)
        self.pre = [0] * (len(nums)+1)
        self.post = [0] * (len(nums)+1)
        for i in range(1, len(nums)):
            self.pre[i] = nums[i-1] + self.pre[i-1]
        for i in range(len(nums)-2, -1, -1):
            self.post[i] = nums[i+1] + self.post[i+1]


    def sumRange(self, left: int, right: int) -> int:
        return self.total - (self.pre[left] + self.post[right])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)