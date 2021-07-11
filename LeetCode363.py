class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        target = k

        suffix_up = [[0 for _ in range(n)] for __ in range(m+1)]
        for i in range(1, m+1):
            for j in range(n):
                suffix_up[i][j] = suffix_up[i-1][j] + matrix[i-1][j]
        
        ans = -2147483648
        for i in range(m):
            for j in range(i+1, m+1):
                suffix_left = [0 for _ in range(n+1)]
                for s in range(1, n+1):
                    suffix_left[s] = suffix_left[s-1] + (suffix_up[j][s-1] - suffix_up[i][s-1])
                    for t in range(s):
                        cur = suffix_left[s] - suffix_left[t]
                        if cur > ans and cur <= target:
                            ans = cur
        return ans 
                    
if __name__ == '__main__':
    matrix = [[2,2,-1]]
    k = 0

    solution = Solution()
    
    print(solution.maxSumSubmatrix(matrix, k))