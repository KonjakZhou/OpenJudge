class Solution:
    def hammingWeight(self, n):
        ans = 0
        while n > 0:
            n = n & (n-1)
            ans += 1
        return ans 