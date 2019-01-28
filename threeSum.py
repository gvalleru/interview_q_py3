class Solution:
    def threeSum(self, nums, target=0):
        # sort the list - nums
        nums.sort()
        # store triplets results in results list
        results = []
        for i in range(len(nums) - 2):
            # if current number is same as previous work then skip to next
            # number in the list to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # create boundaries for sub list to compare
            left, right = i+1, len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                # if sum_ is less than target then move left forward and compare
                if sum_ < target:
                    left += 1
                # else if sum_ is grater than target then move right backward and compare
                elif sum_ > target:
                    right -= 1
                # else sum_ is equal to target
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # Now compare the rest of the sub list
                    # avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # once duplicates are skipped on both left and right then
                    # set new left and right indexes
                    left += 1
                    right -= 1
        return results





