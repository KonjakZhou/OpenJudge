class Solution:
    def numIslands(self, grid):
        def bfs(map, x, y):
            m = len(map)
            n = len(map[0])
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            queue = [(x,y)]

            while len(queue)>0:
                x, y  = queue.pop(0)

                for i in range(4):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    if next_x>=0 and next_x<m and next_y>=0 and next_y<n:
                        if map[next_x][next_y] == "1":
                            queue.append((next_x, next_y))
                            map[next_x][next_y] = "0"
            
            return 


        if len(grid)==0:
            return 0
        
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(grid, i, j)
                    ans += 1
        
        return ans

if __name__=="__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    print(Solution.numIslands(Solution, grid))