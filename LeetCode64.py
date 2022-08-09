# coding=utf-8
# Author: KonjakZhou
# Created At: 周二 09 八月 2022 22:55:56 CST
# MagIc C0de: 77e4ea44d234

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        ans = [[0 for _ in range(n)] for __ in range(m)]
        ans[0][0] = grid[0][0]

        for i in range(1,m):
            ans[i][0] = ans[i-1][0] + grid[i][0]
        
        for j in range(1,n):
            ans[0][j] = ans[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                ans[i][j] = grid[i][j] + (ans[i][j-1] if ans[i][j-1] < ans[i-1][j] else ans[i-1][j])
        
        return ans[m-1][n-1]