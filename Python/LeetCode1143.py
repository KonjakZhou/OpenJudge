class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        if n1==0:
            return 0

        n2 = len(text2)
        if n2==0:
            return 0
        
        f = [[0 for _ in range(n2+1)] for __ in range(n1+1)]
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    f[i][j] = f[i-1][j-1]+1
                else:
                    f[i][j] = f[i-1][j-1]
                    if f[i][j]<f[i-1][j]:
                        f[i][j] = f[i-1][j]
                    if f[i][j]<f[i][j-1]:
                        f[i][j] = f[i][j-1]
        return f[n1][n2]