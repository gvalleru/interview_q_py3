class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        print(nums)
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print(buff_dict)
                print([buff_dict[nums[i]], i])
            else:
                buff_dict[target - nums[i]] = i
                print(buff_dict)
