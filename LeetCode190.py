class Solution:
    def reverseBits(self, n):
        ans = 0 
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n = n>>1
        return ans 