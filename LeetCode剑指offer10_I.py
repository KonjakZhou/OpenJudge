class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a = 0
        b = 1
        for _ in range(2,n+1):
            ans = (a+b) % 1000000007
            a = b 
            b = ans
        return b