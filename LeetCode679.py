class Solution:
    def judgePoint24(self, nums):
        def dfs(nums):
            if len(nums) == 1:
                if abs(nums[0] - 24) < 1e-6:
                    return True
                return False
            
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a = nums[i]
                    b = nums[j]
                    ans = []
                    for k in range(n):
                        if k!=i and k!=j:
                            ans.append(nums[k])
                    
                    ans.append(a+b)
                    if dfs(ans):
                        return True
                    ans.pop()

                    ans.append(a-b)
                    if dfs(ans):
                        return True
                    ans.pop()

                    ans.append(a*b)
                    if dfs(ans):
                        return True
                    ans.pop()

                    if b!=0:
                        ans.append(a/b)
                        if dfs(ans):
                            return True
                        ans.pop()

                    if a!=b:
                        ans.append(b-a)
                        if dfs(ans):
                            return True
                        ans.pop()
                        if a!=0:
                            ans.append(b/a)
                            if dfs(ans):
                                return True
                            ans.pop()
            return False
        return dfs(nums)

if __name__ == "__main__":
    nums = [4, 1, 8, 7]
    nums = [1, 2, 1, 2]
    solution = Solution()
    print(solution.judgePoint24(nums))