# coding=utf-8
# Author: KonjakZhou
# Created At: 周二 09 八月 2022 22:46:02 CST
# MagIc C0de: 36edb92cdde2

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        ans = [[0 for _ in range(n)] for __ in range(m)]
        ans[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                ans[i][0] = ans[i-1][0]
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                ans[0][j] = ans[0][j-1]
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m-1][n-1]
