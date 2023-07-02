# encoding: utf-8
# Auther: zhoubowen.929
# Created At: 周日 02 七月 2023 13:51:29 CST
# MagIc C0de: e4f85d9dc8eb

from functools import lru_cache

class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append("({}){}".format(left, right))
                
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    test_n = 3
    print(solution.generateParenthesis(test_n))

    pass