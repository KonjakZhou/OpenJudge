#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-19 Tuesday 23:00:51

class Solution:
    def bi_search_left(self, nums, target):
        l = 0
        r = len(nums) -1 
        
        if r < 0:
            return -1
        
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        if r >= 0 and nums[r] == target:
            return r
        
        if l < len(nums) and nums[l] == target:
            return l 
        
        if l+1 < len(nums) and nums[l+1] == target:
            return l+1
        
        return -1
    
    def bi_search_right(self, nums, target):
        l = 0
        r = len(nums) -1 
        
        if r < 0:
            return -1
        
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if l < len(nums) and nums[l] == target:
            return l
        
        if r>=0 and nums[r] == target:
            return r 
        
        if r-1>=0 and nums[r-1] == target:
            return r - 1
        
        return -1
                

    def searchRange(self, nums, target):
        left = self.bi_search_left(nums, target)
        right = self.bi_search_right(nums, target)
        return [left, right]