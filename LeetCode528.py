import random
class Solution:

    def __init__(self, w):
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]
        self.total = self.w[-1]

    def pickIndex(self):
        def bisearch(l, r, target):
            if (r - l) <= 1:
                if self.w[l] >= target:
                    return l
                return r

            mid = (l + r) >> 1
            if self.w[mid] >= target:
                r = mid
            else:
                l = mid
            
            return bisearch(l,r,target)

        target = random.randint(1, self.total)
        return bisearch(0, len(self.w)-1, target)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()