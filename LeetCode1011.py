class Solution:
    def shipWithinDays(self, weights, D):
        def check(ans, weights, n, D):
            days = D
            cur = weights[0]
            for i in range(1, n):
                if cur+weights[i]>ans:
                    cur = weights[i]
                    days -= 1
                    if days<=0:
                        return False
                else:
                    cur += weights[i]
            return True
            

        n = len(weights)
        if n==0:
            return 0

        total = 0
        maxx = 0
        for num in weights:
            total += num
            if maxx < num:
                maxx = num
        
        l,r = maxx, total
        while (l<r):
            mid = (l + r) >> 1
            flag = check(mid, weights, n, D)
            if flag:
                r = mid
            else:
                l = mid+1
        return l
        