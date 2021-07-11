class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._matrix = matrix
        self._prefix = self.getPrefix()
        print(matrix)
        print(self._prefix)

    def getPrefix(self):
        m = len(self._matrix)
        # if m==0:
        #     return None
        if m>0:
            n = len(self._matrix[0])
        else:
            n = 0

        result = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1,n+1):
                result[i][j] = -result[i-1][j-1] + result[i][j-1] + result[i-1][j] + self._matrix[i-1][j-1]
        return result

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self._prefix[row2+1][col2+1] - self._prefix[row1][col2+1] - self._prefix[row2+1][col1] + self._prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)

param_1 = obj.sumRegion(2, 1, 4, 3)# -> 8
print(param_1)
param_1 = obj.sumRegion(1, 1, 2, 2)# -> 11
print(param_1)
param_1 = obj.sumRegion(1, 2, 2, 4)# -> 12
print(param_1)