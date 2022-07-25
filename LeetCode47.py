#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-25 星期一 21:59:45

class Solution:
    def permuteUnique(self, nums):
        def dfs(nums, k):
            if k >= len(nums):
                ans.append(ans_tmp[:])
                return 

            for i in range(len(nums)):
                if not flag[i]  and (i == 0 or (nums[i]!=nums[i-1]) or (nums[i]==nums[i-1] and flag[i-1])):
                    ans_tmp.append(nums[i])
                    flag[i] = True
                    dfs(nums, k+1)
                    flag[i] = False
                    ans_tmp.pop()
            return 
        
        ans = list()
        ans_tmp = list()
        flag = [False for _ in nums]
        nums = sorted(nums)
        
        dfs(nums, 0)
        return ans 