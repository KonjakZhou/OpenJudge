import sys

def solve(n, k, x, weights):
    d = list()
    for i in range(n-1):
        if weights[i+1] - weights[i] > x:
            d.append(weights[i+1] - weights[i])
    
    if x == 0:
        return (len(d) + 1)
    
    for i in range(len(d)):
        d[i] = (d[i] - 1) // x
    d.sort()
    ans = len(d) + 1

    # cnt = 0
    # while cnt < len(d) and k >= d[cnt] :
    #     k -= d[cnt]
    #     ans -= 1
    
    for num in d:
        if k >= num:
            ans -= 1
            k -= num

    return ans

if __name__ == "__main__":
    n, k, x = list(map(int, input().strip().split()))
    weights = list(map(int, input().strip().split()))
    weights.sort()
    
    print(solve(n, k, x, weights))
