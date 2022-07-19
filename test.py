import random

def bisearch(arr,  target):
    l = 0
    r = len(arr) - 1
    
    while r - l > 1:
        mid = (l + r) >> 1
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid
        if arr[mid] < target:
            l = mid

    if arr[r] < target:
        return r + 1
    if arr[l] >= target:
        return l
    return r


origin_list = [8, 6, 3, 1, 10]
sum_list = [0 for i in origin_list]
sum_list = [0]
for i in range(len(origin_list)):
  sum_list.append(sum_list[-1] + origin_list[i])
x = random.randint(1, sum_list[-1])
ans = bisearch(sum_list, x) - 1 

print(x)
print(ans)