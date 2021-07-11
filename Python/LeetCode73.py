class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0 :
            return
        n = len(matrix[0])
        if n == 0 :
            return

        flagCol0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                flagCol0 = True
                break
        flagRow0 = False
        for j in range(n):
            if matrix[0][j] == 0:
                flagRow0 = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if flagRow0:
            for j in range(n):
                matrix[0][j] = 0
        if flagCol0:
            for i in range(m):
                matrix[i][0] = 0

        return 

