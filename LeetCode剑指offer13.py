class Solution:
    def movingCount(self, m, n, k):
        def calSum(x,y):
            ans = 0
            while x>0:
                ans += x%10
                x = x//10
            while y>0:
                ans += y%10
                y = y//10
            return ans 
        
        def dfs(x,y,k):
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x>=0 and next_x<m and next_y>=0 and next_y<n and (not flag[next_x][next_y]) and calSum(next_x, next_y)<=k:
                    flag[next_x][next_y] = True
                    dfs(next_x, next_y, k)
            return 

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        flag = [[False for _ in range(n)] for __ in range(m)]
        flag[0][0] = True
        dfs(0,0,k)
        ans = 0
        for i in range(m):
            for j in range(n):
                if flag[i][j]:
                    ans += 1
        return ans 

if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(7,2,3))