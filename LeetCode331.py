class Solution:
    def isValidSerialization(self, preorder):
        inputs = preorder.split(",")
        if len(inputs) == 0:
            return True
        if len(inputs) == 1 and inputs[0] == "#":
            return True
        if inputs[0] == "#":
            return False

        stack_cnt = [0]

        for i in range(1, len(inputs)):
            if inputs[i] == "#":
                stack_cnt[-1] += 1
            else:
                stack_cnt.append(0)

            while stack_cnt[-1] == 2:
                stack_cnt.pop()
                if len(stack_cnt) == 0:
                    if i==len(inputs) - 1:
                        return True
                    return False
                stack_cnt[-1] += 1

        return False
if __name__ == "__main__":
    s = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    s = "1,#"
    s = "9,#,#,1"
    solution = Solution()
    print(solution.isValidSerialization(s))