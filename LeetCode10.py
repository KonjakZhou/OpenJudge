# encoding: utf-8
# Auther: zhoubowen.929
# Created At: 周日 02 七月 2023 14:16:14 CST
# MagIc C0de: 26df073745ae


class Solution:
    def isChrMatch(self, x,y):
        if x==y or y=='.':
            return True
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        flag = [[False for _ in range(n+1)] for __ in range(m+1)]
        flag[0][0] = True

        for j in range(1, n+1):
            cur_p = p[j-1]
            next_p = p[j] if j-1 < n-1 else ''

            if cur_p == '*' or (cur_p != '*' and next_p == '*'):
                flag[0][j] = flag[0][j-1]
            else:
                flag[0][j] == False
            

        for j in range(1, n+1):
            for i in range(1, m+1):
                cur_s = s[i-1]
                cur_p = p[j-1]
                next_p = p[j] if j-1 < n-1 else ''
                last_p = p[j-2] if j-1 > 0 else ""

                if next_p == '*':
                    if self.isChrMatch(cur_s, cur_p):
                        flag[i][j] = flag[i-1][j-1] or flag[i][j-1] or flag[i-1][j]
                    else:
                        flag[i][j] = flag[i][j-1]
                elif cur_p == '*':
                    if self.isChrMatch(cur_s, last_p):
                        flag[i][j] = flag[i-1][j-1] or flag[i][j-1]
                    else: 
                        flag[i][j] = flag[i][j-1]
                elif self.isChrMatch(cur_s, cur_p):
                    flag[i][j] = flag[i-1][j-1]
                else:
                    flag[i][j] = False

        return flag[m][n]
    
if __name__ == '__main__':
    pass