class Solution:
    def isMatch(self, s, p):

        m = len(s)
        n = len(p)
        flag = [ [False for _ in range(n+1)] for __ in range(m+1) ] 
        flag[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                flag[0][j] = flag[0][j-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1]==".":
                    flag[i][j] = flag[i-1][j-1]
                elif p[j-1] == '*' and (p[j-2] == "." or s[i-1] == p[j-2]):
                    flag[i][j] = flag[i][j-2] or flag[i-1][j]
        return flag[m][n]
