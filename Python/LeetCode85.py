class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        M = len(matrix)
        N = len(matrix[0])

        left = [0 for _ in range(N)]
        right = [N-1 for _ in range(N)]
        height = [0 for _ in range(N)]
        maxArea = 0

        for i in range(M):

            currentLeft = 0
            currentRight = N - 1

            # update height
            for j in range(N):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # update left
            for j in range(N):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], currentLeft)
                else:
                    left[j] = 0
                    currentLeft = j+1

            # update right
            for j in range(N-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], currentRight)
                else:
                    right[j] = N-1
                    currentRight = j-1

            # update area
            for j in range(N):
                area = height[j] * (right[j] - left[j] + 1)
                maxArea = max(area, maxArea)

        return maxArea


if __name__ == '__main__':
    matrix = [["0", "1"]]

    solution = Solution()
    ans = solution.maximalRectangle(matrix)
    print(ans)
