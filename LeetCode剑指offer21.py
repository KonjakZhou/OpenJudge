class Solution:
    def exchange(self, nums):
        j = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] & 1 == 1:
                j += 1
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
        t = nums[0]
        nums[0] = nums[j]
        nums[j] = t
        return nums