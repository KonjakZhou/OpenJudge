class Solution:
    def spiralOrder(self, matrix):
        maxRow = len(matrix)
        if maxRow==0 :
            return []
        maxCol = len(matrix[0])
        if maxCol==0:
            return [[]]
        
        minRow = 0
        minCol = 0

        curx = 0
        cury = -1
        direct = 0
        ans = list()
        while minRow < maxRow and minCol < maxCol:
            if direct == 0:
                cury += 1
                ans.append(matrix[curx][cury])
                if cury==maxCol-1:
                    minRow += 1
                    direct = 1
                continue
            if direct == 1:
                curx += 1
                ans.append(matrix[curx][cury])
                if curx == maxRow-1:
                    maxCol -= 1
                    direct = 2
                continue
            if direct == 2:
                cury -= 1
                ans.append(matrix[curx][cury])
                if cury == minCol:
                    maxRow -= 1
                    direct = 3
                continue
            if direct == 3:
                curx -= 1
                ans.append(matrix[curx][cury])
                if curx == minRow:
                    minCol += 1
                    direct = 0
        return ans