class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        
        flag = [[True for _ in range(n+2)] for __ in range(m+2)]
        for i in range(n+2):
            flag[0][i] = False
            flag[m+1][i] = False
        for i in range(m+2):
            flag[i][0] = False
            flag[i][n+1] = False
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        dirct = 0
        x = 1
        y = 1
        ans = list()
        while True:
            ans.append(matrix[x-1][y-1])
            flag[x][y] = False
            
            next_x = x + dx[dirct]
            next_y = y + dy[dirct]
            if flag[next_x][next_y]:
                x = next_x
                y = next_y
                continue
            dirct = (dirct + 1) % 4
            next_x = x + dx[dirct]
            next_y = y + dy[dirct]
            if flag[next_x][next_y]:
                x = next_x
                y = next_y
                continue
            return ans

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    print(solution.spiralOrder(matrix))