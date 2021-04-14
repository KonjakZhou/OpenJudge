class Solution:
    def numTrees(self, n):
        def f(k,flag,n):
            return flag[k-1] * flag[n-k]

        if n<=1:
            return n

        flag = [-1 for i in range(n+1)]
        flag[0] = 1
        flag[1] = 1
        for i in range(2,n+1):
            ans = 0
            for j in range(1,i+1):
                ans += f(j,flag,i)
            flag[i] = ans
        return flag[n]

if __name__=="__main__":
    solution = Solution()
    n = 4
    print(solution.numTrees(n))