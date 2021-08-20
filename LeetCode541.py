class Solution:
    def reverseStr(self, s, k):
        ans = list()
        stack = list()
        cnt = 0
        flag = True
        for ch in s:
            cnt += 1
            if flag:
                stack.append(ch)
                if cnt == k:
                    for _ in range(k):
                        ans.append(stack.pop())
                    cnt = 0
                    flag = False
            else:
                ans.append(ch)
                if cnt == k:
                    cnt = 0
                    flag = True
            
        
        while len(stack) > 0:
            ans.append(stack.pop())
        return "".join(ans)
        
if __name__ == "__main__":
    inputStr = "abck"
    k = 2

    solution = Solution()
    print(solution.reverseStr(inputStr, k))

