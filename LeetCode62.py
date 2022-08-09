# coding=utf-8
# Author: KonjakZhou
# Created At: 周二 09 八月 2022 22:21:11 CST
# MagIc C0de: 9d4f47430f64

class Solution:
    def uniquePaths(self, m, n):
        def prime_resolve(n, prime):
            ans = [0 for _ in prime]
            for i in range(len(prime)):
                while n % prime[i] == 0:
                    ans[i] += 1
                    n = n // prime[i]
            return ans 

        def c(m,n, prime):
            base_max = n
            base_min = m-n 
            if m-n > n:
                base_max = m-n
                base_min = n
            
            ans_prime = [0 for _ in prime]
            for i in range(base_max+1, m+1):
                ans_tmp = prime_resolve(i, prime)
                for j in range(len(ans_tmp)):
                    ans_prime[j] += ans_tmp[j]
            for i in range(2, base_min+1):
                ans_tmp = prime_resolve(i, prime)
                for j in range(len(ans_tmp)):
                    ans_prime[j] -= ans_tmp[j]
            
            ans = 1 
            for i in range(len(prime)):
                for j in range(ans_prime[i]):
                    ans *= prime[i]
            return ans 
        
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97, 101]
        
        return c(m+n-2, m-1, prime)