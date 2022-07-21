#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-21 星期四 22:42:22

class Solution:                
    def combinationSum(self, candidates, target):
        def dfs(candidates, target, k):
            if target == 0:
                ans.append(ans_tmp[:])
                return 
            
            if k >= len(candidates):
                return 

            cnt = 0
            dfs(candidates, target, k+1)
            while target >= candidates[k]:
                ans_tmp.append(candidates[k])
                dfs(candidates, target - candidates[k], k+1)
                target -= candidates[k]
                cnt += 1

            for i in range(cnt):
                ans_tmp.pop()
            return 

        ans_tmp = list()
        ans = list()
        dfs(candidates, target, 0)
        return ans 