class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        total = n
        j = 0
        for i in range(n):
            if val == nums[i]:
                total -= 1
            else:
                nums[j] = nums[i]
                j += 1
        return total