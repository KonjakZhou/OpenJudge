def getFather(x, father):
    if father[x] == x:
        return father[x]
    return getFather(father[x], father)

def union(x,y,father):
    father[x] = y
    return 

n, k = map(int, input().strip().split())

father = [i for i in range(n)]
ans = [0 for _ in range(n)]
for i in range(k):
    a, b = map(int, input().strip().split())
    if a==b:
        father[a-1] = a-1
    else:
        union(a-1, b-1, father)
for i in range(n):
    ans[getFather(i, father)]+=1

maxx = 0
for i in range(n):
    if maxx<ans[i]:
        maxx = ans[i]
print(maxx)