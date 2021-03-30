from math import sqrt

def init():
    citys = list()

    n, c = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        citys.append((x,y))

    if n <= 1:
        dist = None

    dist = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            distance = sqrt((citys[i][0] - citys[j][0])**2 + (citys[i][1] - citys[j][1])**2)
            dist[i][j] = distance
            dist[j][i] = distance
    
    return n,c,dist

def prim(map, n, c):
    if n<=1:
        return 0

    flag = [False for _ in range(n)]
    flag[0] = True

    dist = [map[0][i] for i in range(n)]

    have_airports = c
    no_airports = 0

    for _ in range(n-1):
        min_index = -1
        min_value = 2147483647
        for i in range(n):
            if not flag[i] and min_value>dist[i]:
                min_value = dist[i]
                min_index = i
        ans_tmp = no_airports + 2*c
        if ans_tmp > have_airports + c:
            ans_tmp = have_airports + c
        if ans_tmp > have_airports + min_value:
            ans_tmp = have_airports + min_value
        have_airports = ans_tmp
        no_airports = no_airports + min_value

        flag[min_index] = True
        for i in range(n):
            if not flag[i] and dist[i]>map[min_index][i]:
                dist[i] = map[min_index][i]

    if have_airports < no_airports:
        return have_airports
    return no_airports

if __name__ == "__main__":
    n, c, dist = init()
    ans = prim(dist, n, c)
    print(ans)