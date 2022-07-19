def solve(a, b, f, k):
    if k == 1:
        if b < f or b < (a - f):
            return -1
        if b < a:
            return 1
        return 0
    
    if k == 2:
        if b < f or b < 2 * (a - f):
            return -1
        
        if b < a + a - f or b < a + f:
            return 2
        
        if b < 2 * a : 
            return 1
        
        return 0 

    if k > 2:
        if b < 2*f or b < 2*(a - f):
            return -1

    ans = 0
    cur = b
    for i in range(k):
        if i == k-1:
            if cur < a:
                ans += 1
        else:
            if i & 1 == 0:
                if cur < a + (a - f):
                    ans += 1
                    cur = b - (a - f)
                else:
                    cur = cur - a
            else:
                if cur < a + f:
                    ans += 1
                    cur = b - f
                else:
                    cur = cur - a
    return ans 

if __name__ == "__main__":
    a, b, f, k = list(map(int, input().strip().split()))
    print(solve(a, b, f, k))
    