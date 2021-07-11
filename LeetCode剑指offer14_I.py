class Solution:
    def cuttingRope(self, n):
        f = [[0 for _ in range(n+1)] for __ in range(n+1)]
        
        f[2][2] = 1
        f[3][2] = 2
        for i in range(4, n+1):
            max_ans = i
            for k in range(1,i):
                cur_ans = (i-k) * k
                if max_ans < cur_ans:
                    max_ans = cur_ans
            f[i][2] = max_ans

        for i in range(3,n+1):
            for j in range(3, i+1):
                max_ans = f[i][j-1]
                for k in range(1, i-1):
                    cur_ans = f[i-k][j-1] * k 
                    if max_ans<cur_ans:
                        max_ans = cur_ans
                f[i][j] = max_ans
        return f[n][n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.cuttingRope(10))