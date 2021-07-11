class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        result = [[0 for _ in range(n+1)] for __ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                result[i][j] = max(result[i-1][j], result[i][j-1]) + grid[i-1][j-1]
        return result[m][n]
     