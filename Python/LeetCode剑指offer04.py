class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if len(matrix)==0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        sx = 0
        sy = n-1
        
        while True:
            if target == matrix[sx][sy]:
                return True
            if target > matrix[sx][sy]:
                sx += 1
                if sx>=m:
                    return False
            else:
                sy -= 1
                if sy<0:
                    return False
