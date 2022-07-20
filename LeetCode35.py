#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-20 星期三 22:01:10

class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1 
        while r - l > 1:
            mid = (l + r ) >> 1
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid
            else:
                l = mid 

        if nums[l] >= target:
            return l
        if nums[r] >= target:
            return r
        
        if nums[r] < target:
            return r + 1