class Solution:
    def nthSuperUglyNumber(self, n: int, primes):
        pointers = [ 1 for _ in primes]

        ans = [0 for _ in range(n+1)]
        ans[1] = 1

        for i in range(2,n+1):
            min_tmp = 2147483647
            min_pos = -1
            for j,prime in enumerate(primes):
                if min_tmp < ans[pointers[j]] * prime:
                    min_tmp = ans[pointers[j]] * prime
                    min_pos = j
            ans[i] = min_tmp
            pointers[min_pos] = i
        return ans[n]
