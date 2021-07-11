class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        if n==0:
            return []
        stack = list()

        flag = [False for _ in range(n)]
        ans = [0 for _ in range(n)]
        for i in range(n*2):
            curIndex = i % n
            while len(stack)>0:
                if nums[curIndex] > nums[stack[-1]]:
                    lastIndex = stack.pop()  
                    if not flag[lastIndex]:
                        flag[lastIndex] = True
                        ans[lastIndex] = nums[curIndex]
                else:
                    break
            stack.append(curIndex)
            
        for i in range(n):
            if not flag[i]:
                ans[i] = -1
        return ans 

if __name__ == "__main__":
    input = [1,2,1]
    solution = Solution()
    print(solution.nextGreaterElements(input))
