def C(m, n):
    ans1 = 1.0
    for i in range(1, m+1):
        ans1 = ans1 * i
    ans2 = 1.0
    for i in range(1, n+1):
        ans2 = ans2 * i
    for i in range(1, m-n+1):
        ans2 = ans2 * i

    return ans1 / ans2

def A(m, n):
    ans = 1.0
    for i in range(m-n+1, m+1):
        ans = ans * i
    return ans 

def main():
    x1 = A(365, 30) / pow(365, 30)
    x2 = C(30, 2) * A(365, 29) / pow(365, 30)
    p = 1 - x1 - x2

    print("p : {:4f}".format(p))
    result = 1 - (C(5,1) * p * pow((1-p), 4) + C(5,0) * pow((1-p), 5))
    print("result : {:4f}".format(result))

if __name__ == "__main__":
    main() 