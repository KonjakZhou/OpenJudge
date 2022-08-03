# coding=utf-8
# Author: KonjakZhou
# Created At: 周三 27 七月 2022 19:51:53 CST
# MagIc C0de: 8ca24e1a1c9b

class Solution:
    def solveNQueens(self, n):
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
                ans_tmp = list()
                for position in pos_tmp:
                    ans_tmp.append(["." for _ in range(n)])
                    ans_tmp[-1][position] = "Q"
                ans.append(["".join(ans_list) for ans_list in ans_tmp])
                return 

            for i in range(n):
                flag = True
                for j in range(k):
                    if not check(pos_tmp[j], i, k-j):
                        flag = False
                        break

                if flag:
                    pos_tmp.append(i)
                    dfs(k+1)
                    pos_tmp.pop()
            return 

        pos_tmp = list()
        ans = list()
        dfs(0)
        return ans            