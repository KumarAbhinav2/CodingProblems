class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.numArray(nums)

    def numArray(self, nums):
        self.ssum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.ssum[i + 1] = self.ssum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.ssum[right+1] - self.ssum[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))