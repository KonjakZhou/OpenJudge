#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-23 星期六 23:15:09

class Solution:
    def isMatch(self, s, p):
        ls = len(s)
        lp = len(p)

        s = "-"+s
        p = "_"+p
        f = [[False for _ in range(lp+1)] for __ in range(ls+1)]
        f[0][0] = True
        
        for j in range(1, lp+1):
            if p[j] == '*':
                f[0][j] = True
            else:
                break
                
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if s[i] == p[j] or p[j] == '?':
                    f[i][j] = f[i-1][j-1]
                elif p[j] == '*':
                    f[i][j] = f[i-1][j-1] or f[i-1][j] or f[i][j-1]
        
        return f[ls][lp]
