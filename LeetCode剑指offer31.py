class Solution:
    def validateStackSequences(self, pushed, popped):
        n = len(pushed)
        if n == 0:
            return True
        
        stack = list()
        cnt = 0
        for ele in popped:
            while len(stack)==0 or stack[-1]!=ele:
                if cnt == n:
                    return False
                stack.append(pushed[cnt])
                cnt += 1
            stack.pop()
        return True