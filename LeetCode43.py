#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-23 星期六 00:35:23

class Solution:
    def multiply(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        num1 = [ord(num1[len1-k-1]) - 48 for k in range(len1)]
        num2 = [ord(num2[len2-k-1]) - 48 for k in range(len2)]

        ans = [0 for _ in range(len1 + len2 + 1)]
        for i in range(len1):
            for j in range(len2):
                ans[i + j] += num1[i] * num2[j]
        
        for i in range(len(ans)-1):
            ans[i+1] += ans[i] // 10
            ans[i] = ans[i] % 10

        k = len(ans) - 1
        while k >= 0 and ans[k] == 0:
            k -= 1
        if k < 0:
            return "0"
        ans = [chr(ans[k - i] + 48) for i in range(k+1)]
        return "".join(ans) 