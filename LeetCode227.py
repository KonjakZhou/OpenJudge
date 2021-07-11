class Solution:
    def calculate(self, s):
        s = "(" + "".join(s.split(" ")) + ")"
        stack_num = list()
        stack_sym = list()
        priority = {"(":0, "+":1, "-":1, "*":2, "/":2}
        num_register = 0
        flag = False
        for ch in s:
            if 48 <= ord(ch) < 58:
                num_register = num_register * 10 + ord(ch) - 48
                flag = True
            else:
                if flag:
                    stack_num.append(num_register)
                    flag = False
                    num_register = 0
                if ch == "(":
                    stack_sym.append("(")
                elif ch == ")":
                    while stack_sym[-1] != "(":
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        symbol = stack_sym.pop()
                        if symbol == "+":
                            stack_num.append(num1 + num2)
                        elif symbol == "-":
                            stack_num.append(num1 - num2)
                        elif symbol == "*":
                            stack_num.append(num1 * num2)
                        else:
                            stack_num.append(num1 // num2)
                    stack_sym.pop()
                else:
                    while len(stack_sym)>0 and priority[ch] <= priority[stack_sym[-1]]:
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        symbol = stack_sym.pop()
                        if symbol == "+":
                            stack_num.append(num1 + num2)
                        elif symbol == "-":
                            stack_num.append(num1 - num2)
                        elif symbol == "*":
                            stack_num.append(num1 * num2)
                        else:
                            stack_num.append(num1 // num2)
                    stack_sym.append(ch)
        return stack_num[-1]

if __name__ == "__main__":
    s = "3+2*2"
    s = " 3+5 / 2 "
    s = " 3/2 "
    solution = Solution()
    print(solution.calculate(s))
            
        
        