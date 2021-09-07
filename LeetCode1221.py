class Solution:
    def balancedStringSplit(self, s):
        stack = list()
        ans = 0
        cur_start = None

        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
                cur_start = ch
                ans += 1
                continue
            
            if cur_start == ch:
                stack.append(ch)
            else:
                stack.pop()
        return ans 