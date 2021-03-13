class Solution:
    def findRepeatNumber(self, nums):
        flag = [False for _ in range(nums)]
        for i in nums:
            if not flag[i]:
                flag[i] = True
            else: 
                return i