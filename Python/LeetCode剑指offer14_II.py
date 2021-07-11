class Solution:
    def cuttingRope(self, n):
        def quictPow(a, m):
            ans = 1
            cur_a = a
            while m > 0:
                if m & 1 == 1:
                    m -= 1 
                    ans = ans * cur_a % 1000000007
                else:
                    cur_a = cur_a * cur_a % 1000000007
                    m = m >> 1
            return ans 

        if n == 2:
            return 1
        if n == 3:
            return 2
        if n==4:
            return 4
        
        times, res = divmod(n, 3)
        
        if res == 0:
            return quictPow(3, times)
        if res == 1:
            return quictPow(3, times-1) * 4 % 1000000007
        if res == 2:
            return quictPow(3, times) * 2 % 1000000007



if __name__ == "__main__":
    solution = Solution()
    print(solution.cuttingRope(10))

