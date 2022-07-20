class Solution:
    def check_board(self, check_list):
        a = [0 for _ in range(10)]
        for num_str in check_list:
            num = ord(num_str) - 48
            if 0 <= num <= 9:
                a[num] += 1
                if a[num] > 1:
                    return False
        
        return True

                
    def isValidSudoku(self, board):
        
        for i in range(9):
            check_list_row = list()
            check_list_col = list()
            check_list_square = list()
            for j in range(9):
                check_list_row.append(board[i][j])
                check_list_col.append(board[j][i])
                check_list_square.append(board[i // 3 * 3 + j // 3][i % 3 * 3  + j % 3])
            
            if not self.check_board(check_list_row):
                return False
            if not self.check_board(check_list_col):
                return False
            if not self.check_board(check_list_square):
                return False
        
        
        return True