class Solution:
    def findMinArrowShots(self, points):
        N = len(points)
        points.sort(key=lambda x: x[0])
        flag = [1 for _ in range(N)]

        ans = 0
        for i in range(N):
            if flag[i]:
                ans += 1
                flag[i] = 0
                area = points[i]
                for j in range(i + 1, N):
                    if points[j][0] <= area[1]:
                        flag[j] = 0
                        area = points[j][0], min(area[1], points[j][1])
        return ans


if __name__ == '__main__':
    points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9],
              [0, 6], [2, 8]]

    solution = Solution()
    ans = solution.findMinArrowShots(points)
    print(ans)
