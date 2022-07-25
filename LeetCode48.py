#!/usr/bin/env python
# coding=utf-8
# Author: zhoubowen
# Created Time: 2022-07-25 星期一 22:46:05

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        def trans(a):
            b = [
                [0, -1],
                [1, 0]
            ]

            length = len(a)
            ans = [0,0]
            for i in range(length):
                for j in range(length):
                    ans[i] += a[j] * b[j][i]
            return ans
        
        def mapping(a):
            return a[0], a[1] + length - 1
        
        length = len(matrix)
        flag = [[False for _ in range(length)] for __ in range(length)]

        for i in range(length):
            for j in range(length):
                s = [i,j]
                tmp_last = matrix[i][j]
                tmp_now = None
                while not flag[s[0]][s[1]]:
                    flag[s[0]][s[1]] = True
                    next_x, next_y = mapping(trans(s))
                    if flag[next_x][next_y]:
                        matrix[next_x][next_y] = tmp_last
                    else:
                        tmp_now = matrix[next_x][next_y]
                        matrix[next_x][next_y] = tmp_last
                        tmp_last = tmp_now
                        s = [next_x, next_y]
                    
        return 