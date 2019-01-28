class Solution:
    def __init__(self, nums):
        self.nums = nums

    def _find_split_point(self):
        left_sum = right_sum = 0

        for i in range(len(self.nums)):
            left_sum += self.nums[i]

        if left_sum % 2 != 0:
            return -1
        for i in range(len(self.nums) - 1, -1, -1):
            right_sum += self.nums[i]
            left_sum -= self.nums[i]
            if left_sum == right_sum:
                return i
        return -1

    def split_array_two(self):
        split_point = self._find_split_point()
        print("list: ", self.nums)
        if split_point == -1 or split_point == len(self.nums):
            return "Can't split"
        else:
            return self.nums[:split_point], self.nums[split_point:]
