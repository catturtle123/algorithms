import heapq
n, m, r = map(int, input().split(' '))
tlist = list(map(int, input().split(' ')))

def floyd_warshall():
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i in range(r):
        a, b, l = map(int, input().split(' '))
        dist[a - 1][b - 1] = l
        dist[b - 1][a - 1] = l

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    maxs = 0
    sum = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            if dist[i][j] <= m:
                sum += tlist[j]
        maxs = max(maxs, sum)

    print(maxs)

floyd_warshall()

