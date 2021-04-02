from math import sqrt

def init():
    citys = list()
    edges = list()

    n, c = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        citys.append((x,y))

    for i in range(n):
        for j in range(i+1,n):
            distance = sqrt((citys[i][0] - citys[j][0])**2 + (citys[i][1] - citys[j][1])**2)
            edges.append((i,j,distance))
    
    return n,c, edges

def getFather(x, father):
    if father[x] == x:
        return x
    father[x] = getFather(father[x], father)
    return father[x] 

def union(x,y, father):
    xFather = getFather(x, father)
    yFather = getFather(y, father)
    father[xFather] = yFather
    return 

def isUnion(x,y, father):
    xFather = getFather(x, father)
    yFather = getFather(y, father)
    return xFather==yFather

def kruskal(n, c, edges):
    if n<=1:
        return 0
    edges.sort(key=lambda x: x[-1])

    father = [i for i in range(n)]

    cost = n*c
    ans = n*c
    cnt_edge = 0

    for _ in range(n-2):
        while True:
            x = edges[cnt_edge][0]
            y = edges[cnt_edge][1]
            w = edges[cnt_edge][2]
            cnt_edge += 1
            if isUnion(x, y, father):
                continue
            union(x, y, father)
            cost = cost - c + w
            if ans > cost:
                ans = cost
            break
    while True:
        x = edges[cnt_edge][0]
        y = edges[cnt_edge][1]
        w = edges[cnt_edge][2]
        cnt_edge += 1
        if isUnion(x, y, father):
            continue
        union(x, y, father)
        cost = cost - c * 2 + w
        if ans > cost:
            ans = cost
        break
    
    return ans

if __name__ == "__main__":
    n, c, edges = init()
    ans = kruskal(n, c, edges)
    print(ans)