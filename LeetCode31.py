# encoding: utf-8
# Auther: zhoubowen.929
# Created At: Mon 18 July 2022 22:46:23 CST
# MagIc C0de: 2f5dee5f2959

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                break
        
        flag = 0
        for j in range(i, len(nums)):
            if nums[i-1] >= nums[j]:
                t = nums[i-1]
                nums[i-1] = nums[j-1]
                nums[j-1] = t
                flag = 1
                break
        
        if flag == 0:
            t = nums[i-1]
            nums[i-1] = nums[j]
            nums[j] = t
                
        s = i 
        for i in range(len(nums)-1, s, -1):
            for j in range(s, i):
                if nums[j]>nums[i]:
                    t = nums[j]
                    nums[j] = nums[i]
                    nums[i] = t
        
        return 
                    
if __name__ == '__main__':
    ans = [5,3,4,2,1]
    solution = Solution()
    solution.nextPermutation(ans)
    print(ans)
    pass