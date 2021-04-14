mod = 1000000007

n, m = list(map(int, input().strip().split()))

a = list(map(int, input().strip().split()))
d = [a[0]] + [a[i]-a[i-1] for i in range(1,n)]
y = [d[0]] + [d[i]-d[i-1] for i in range(1,n)]

for i in range(m):
    i,j,b = list(map(int, input().strip().split()))
    i-=1
    j-=1
    y[i] += b

    if j<n-1:
        y[j+1] -= (j-i+2)*b
    if j<n-2:
        y[j+2] += (j-i+1)*b

d = [y[0]]
for i in range(1,n):
    d.append(d[-1]+y[i])
a = [d[0]]
for i in range(1,n):
    a.append(a[-1]+d[i])
print(a)
