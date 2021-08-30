def bisearch(l, r, target, w):
    if (r - l) <= 1:
        if w[l] >= target:
            return l
        return r

    mid = (l + r) >> 1
    print(l," ", r, " ", mid)
    if w[mid] >= target:
        r = mid
    else:
        l = mid
    
    return bisearch(l,r,target, w)

if __name__ == "__main__":
    a = [3,3,3,3,3]
    print(bisearch(0, len(a)-1, 2, a))