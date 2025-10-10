import sys

INF = sys.maxsize

input = sys.stdin.readline

n = int(input()) # 도시의 갯수
m = int(input()) # 버스의 갯수

maps = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            maps[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    maps[a][b] = min(maps[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if maps[i][j] == INF:
            print(0, end=" ")
        else:
            print(maps[i][j], end=" ")
    print()