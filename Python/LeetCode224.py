class Solution:
    def calculate(self, s):
        input_s = "".join(s.split(" "))
        input_s = "(" + input_s + ")"
        processed_s = list()
        for i in range(len(input_s)):
            if input_s[i] == "-":
                if i==0 or input_s[i-1] == "(":
                    processed_s.append("0")
            processed_s.append(input_s[i])
        s = "".join(processed_s)
                
        number_stack = list()
        symbol_stack = list()
        priority = {"(": 0, "-": 1, "+": 1}


        num_register = 0
        flag = False
        for ch in s:
            if ord("0") <= ord(ch) <= ord("9"):
                num_register = num_register * 10 + ord(ch) - 48
                flag = True
                continue
            else:
                if flag:
                    number_stack.append(num_register)
                    num_register = 0
                    flag = False
        
            if ch == "(":
                symbol_stack.append(ch)
            elif ch == ")":
                while symbol_stack[-1] != "(":
                    cur_symbol = symbol_stack.pop()
                    num1 = number_stack.pop()
                    num2 = number_stack.pop()
                    if cur_symbol == "+":
                        number_stack.append(num1 + num2)
                    else:
                        number_stack.append(num2 - num1)
                symbol_stack.pop()
            else:
                while len(symbol_stack)>0 and priority[ch]<=priority[symbol_stack[-1]]:
                    cur_symbol = symbol_stack.pop()
                    num1 = number_stack.pop()
                    num2 = number_stack.pop()
                    if cur_symbol == "+":
                        number_stack.append(num1 + num2)
                    else:
                        number_stack.append(num2 - num1)
                symbol_stack.append(ch)

        return number_stack[0]

if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+8)"
    solution = Solution()
    print(solution.calculate(s))