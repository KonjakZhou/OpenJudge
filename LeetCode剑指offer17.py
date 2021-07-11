class Solution:
    def printNumbers(self, n):
        aim = 1
        for _ in range(n):
            aim = aim * 10
        
        ans = [i for i in range(1,aim)]
        return ans 