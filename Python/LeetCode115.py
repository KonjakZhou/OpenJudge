class Solution:
    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)

        f = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for j in range(n + 1):
            f[0][j] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if t[i-1] == s[j-1]:
                    f[i][j] = f[i-1][j-1] + f[i][j-1]
                else:
                    f[i][j] = f[i][j-1]
        return f[m][n]
