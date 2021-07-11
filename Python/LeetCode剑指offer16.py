class Solution:
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        ans = 1
        cur_x = x
        while (n>0):
            if n & 1 == 1:
                ans = ans * cur_x
                n -= 1
            else:
                n = n >> 1
                cur_x = cur_x * cur_x 
        return ans