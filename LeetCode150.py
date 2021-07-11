class Solution:
    def evalRPN(self, tokens):
        def str2num(string):
            ans = 0
            sig = 1
            start = 0
            n = len(string)
            if string[0] == '-':
                sig = -1
                start = 1
            for i in range(start, n):
                ans = ans * 10 + ord(string[i]) - 48
            return ans * sig

        stack = []
        for ch in tokens:
            if ch == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif ch == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if num1*num2<0:
                    stack.append(num1 // (-num2) * (-1))
                else:
                    stack.append(num1 // num2)
            elif ch == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif ch == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            else:
                stack.append(str2num(ch))
        
        return stack[0]