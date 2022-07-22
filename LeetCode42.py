#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-22 星期五 23:39:50

class Solution:
    def trap(self, height):
        stack = list()
        stack_pos = list()
        ans = 0 
        for pos, h in enumerate(height):
            if len(stack) == 0:
                stack.append(h)
                stack_pos.append(pos)
            elif len(stack) == 1:
                if h >= stack[-1]:
                    stack[-1] = h
                    stack_pos[-1] = pos
                else:
                    stack.append(h)
                    stack_pos.append(pos)
            else:
                while len(stack) > 1 and h > stack[-1]:
                    ans += (min(stack[-2], h) - stack[-1]) * (pos - stack_pos[-2] - 1)
                    stack.pop()
                    stack_pos.pop()
                if h >= stack[-1]:
                    stack.pop()
                    stack_pos.pop() 
                stack.append(h)
                stack_pos.append(pos)
                
        return ans 