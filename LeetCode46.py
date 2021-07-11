class Solution:
    def permute(self, nums):
        def dfs(k):
            if k == n:
                result.append(ans[:])
                return 
            
            for i in range(n):
                if not flag[i]:
                    ans.append(nums[i])
                    flag[i] = True
                    dfs(k+1)
                    flag[i] = False
                    ans.pop()
            return 

        ans = list()
        result = list()
        n = len(nums)
        flag = [False for _ in range(n)]

        dfs(0)
        return result