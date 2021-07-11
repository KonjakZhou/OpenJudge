class Solution:
    def exist(self, board, word):
        def dfs(x,y,cnt_ch):
            if cnt_ch == n_word - 1:
                return True
            next_cnt_ch = cnt_ch + 1
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if next_x>=0 and next_x<m and next_y>=0 and next_y<n and flag[next_x][next_y] and board[next_x][next_y]==word[next_cnt_ch]:
                    flag[next_x][next_y] = False
                    ans = dfs(next_x, next_y, next_cnt_ch)
                    if ans:
                        return True
                    flag[next_x][next_y] = True
            return False
        
        m = len(board)
        n = len(board[0])
        n_word = len(word)
        if n_word == 0:
            return True
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag = [[True for _ in range(n)] for __ in range(m)]
                    flag[i][j] = False
                    ans = dfs(i,j,0)
                    if ans:
                        return True
        return False
        
if __name__ == "__main__":
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    
    soluton = Solution()
    print(soluton.exist(board, word))