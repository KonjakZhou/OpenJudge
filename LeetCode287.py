class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        flag = [False for _ in range(n)]

        for num in nums:
            if not flag[num]:
                flag[num] = True
            else:
                return num