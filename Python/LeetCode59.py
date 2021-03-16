class Solution:
    def generateMatrix(self, n):
        if n == 0:
            return [[]]
        
        flag = [[True for _ in range(n+2)] for __ in range(n+2)]
        for i in range(n+2):
            flag[0][i] = False
            flag[n+1][i] = False
            flag[i][0] = False
            flag[i][n+1] = False

        ans = [[0 for _ in range(n)] for __ in range(n)]
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        dirt = 0
        x = 0
        y = 0
        ans[x][y] = 1
        flag[1][1] = False
        for i in range(2, n*n+1):
            next_x = x + dx[dirt]
            next_y = y + dy[dirt]
            if not flag[next_x+1][next_y+1]:
                dirt = (dirt+1) % 4
                next_x = x + dx[dirt]
                next_y = y + dy[dirt]
            x = next_x
            y = next_y
            ans[x][y] = i
            flag[x+1][y+1] = False
        return ans 

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))