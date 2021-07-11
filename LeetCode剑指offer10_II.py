class Solution:
    def numWays(self, n):
        if n==0:
            return 1
        if n==1:
            return 1
        
        a = 1
        b = 1
        for _ in range(2, n+1):
            ans = (a+b) % 1000000007
            a = b
            b = ans
        return b 