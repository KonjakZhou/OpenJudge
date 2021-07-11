class Solution:
    def addStrings(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        maxLen = max(len1, len2) + 1
        ans = [0 for _ in range(maxLen)]
        
        num1 = [ord(num1[i]) - 48 for i in range(len1-1, -1, -1)]
        num2 = [ord(num2[i]) - 48 for i in range(len2-1, -1, -1)]

        num1.extend([0 for _ in range(maxLen - len1)])
        num2.extend([0 for _ in range(maxLen - len2)])

        for i in range(maxLen):
            ans[i] = num1[i] + num2[i]

        for i in range(maxLen-1):
            ans[i+1] = ans[i+1] + ans[i] // 10
            ans[i] = ans[i] % 10

        for i in range(maxLen-1, -1, -1):
            if ans[i] != 0:
                break
        ansStr = [chr(ans[i] + 48) for i in range(i, -1, -1)]
        
        return "".join(ansStr) 

if __name__ == "__main__":
    num1 = "0"
    num2 = "0"
    solution = Solution()
    print(solution.addStrings(num1, num2))