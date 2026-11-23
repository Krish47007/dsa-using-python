class NumArray:

    def __init__(self, nums: list[int]):
        n = len(nums)
        self.pf = [0] * n
        self.pf[0] = nums[0]
        for i in range(1, n):
            self.pf[i] = self.pf[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pf[right]
        else:
            return self.pf[right] - self.pf[left - 1]

obj = NumArray([1,2,3,4,5])
print(obj.sumRange(2,3))
print(obj.sumRange(0,4))
print(obj.sumRange(1,4))