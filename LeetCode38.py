#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-21 星期四 22:29:14

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        last_ans = self.countAndSay(n-1) + '-'
        
        last_ch = '-'
        ans = ""
        cnt = 0
        for ch in last_ans:
            if ch != last_ch:
                ans += str(cnt) + last_ch
                cnt = 1
            else:
                cnt += 1
            last_ch = ch
        
        return ans[2:] 