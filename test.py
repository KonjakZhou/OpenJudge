from math import exp
from scipy.special import comb, perm
from scipy.stats import poisson
# perm(3,2)     #计算排列数    6

# comb(3,2)   #计算组合数     3


if __name__ == "__main__":
    ans = 0
    for i in range(101, 107):
        ans += poisson.pmf(i, 212 / 2 * 0.95 * 0.95)
    print(ans)

    ans = 0
    for i in range(101, 107):
        ans += comb(106, i) * pow(0.95 * 0.95, i) * pow(1 - 0.95 * 0.95, 106-i)
    print(ans)
