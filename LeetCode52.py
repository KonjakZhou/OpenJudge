# coding=utf-8
# Author: KonjakZhou
# Created At: 周三 03 八月 2022 22:09:24 CST
# MagIc C0de: da2f52b63a34

class Solution:
    def totalNQueens(self, n):
        def check(a,b, dis):
            if a == b:
                return False
            if b - a == dis:
                return False
            if a - b == dis:
                return False
            return True

        def dfs(k):
            if k >= n:
                return 1 
            ans = 0
            for i in range(n):
                flag = True
                for j in range(k):
                    if not check(pos_tmp[j], i, k-j):
                        flag = False
                        break

                if flag:
                    pos_tmp.append(i)
                    ans += dfs(k+1)
                    pos_tmp.pop()
            return ans

        pos_tmp = list()
        return dfs(0)      