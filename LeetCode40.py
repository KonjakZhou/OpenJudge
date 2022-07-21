#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-21 星期四 23:18:02

class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(target, k):
            if target == 0:
                ans.append(ans_tmp[:])
                return 
            
            if k >= len(candidates_once): 
                return 
            
            dfs(target, k+1)
            
            cnt = 0
            for _ in range(1, count[candidates_once[k]]+1):
                if target >= candidates_once[k]:
                    ans_tmp.append(candidates_once[k])
                    dfs(target - candidates_once[k], k+1)
                    cnt += 1
                    target -= candidates_once[k]

            for _ in range(cnt):
                ans_tmp.pop()

            return 
        
        count = dict()
        for num in candidates:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        candidates_once = list(count.keys())
        ans_tmp = list()
        ans = list()
        dfs(target, 0)
        return ans 