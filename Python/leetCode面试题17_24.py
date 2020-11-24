class Solution:
    def getMaxMatrix(self, matrix):
        M = len(matrix)
        N = len(matrix[0])
        ans = [0 for _ in range(4)]

        sumCol = [[0 for _ in range(N)] for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                sumCol[i+1][j] = sumCol[i][j] + matrix[i][j]

        maxValue = float('-inf')
        for i in range(M):
            for j in range(i+1, M+1):
                pre = float('-inf')
                start = -1
                for k in range(0,N):
                    cur = sumCol[j][k] - sumCol[i][k]
                    if pre + cur > cur:
                        pre += cur
                    else:
                        pre = cur
                        start = k

                    if maxValue < pre:
                        maxValue = pre
                        ans[0] = i
                        ans[1] = start
                        ans[2] = j-1
                        ans[3] = k
        return ans

if __name__=="__main__":
    inputs = [[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]
    solution = Solution()
    ans = solution.getMaxMatrix(inputs)
    print(ans)