# coding=utf-8
# Author: KonjakZhou
# Created At: 周四 04 八月 2022 00:14:58 CST
# MagIc C0de: 299a68b3d644

class Solution:
    def getPermutation(self, n, k):
        jc = [1]
        for i in range(1, n+2):
            jc.append(i * jc[-1])
        
        ans = list()
        flag = [True for _ in range(n+1)]
        for i in range(n):
            for j in range(1,n-i+1):
                if k <= j * jc[n-i-1]:
                    break
            cnt = 1
            for _ in range(j):
                while not flag[cnt]:
                    cnt += 1
                cnt += 1
            ans.append(chr(48 + cnt-1))
            flag[cnt-1] = False
            k -= (j-1)*jc[n-i-1]
            
        return "".join(ans)

if __name__ == '__main__':
    n = 3
    k = 1
    solution = Solution()
    print(solution.getPermutation(n,k))