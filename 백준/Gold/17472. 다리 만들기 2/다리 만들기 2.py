import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(sy, sx, idx):
    q = deque()
    q.append((sy, sx))
    board[sy][sx] = idx

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                board[ny][nx] = idx
                q.append((ny, nx))

# 1. 섬 라벨링
island_idx = 2
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            bfs(y, x, island_idx)
            island_idx += 1

island_count = island_idx - 2
INF = sys.maxsize

dist = [[INF] * island_idx for _ in range(island_idx)]

# 2. 행 스캔
for y in range(n):
    start = 0
    length = 0

    for x in range(m):
        if board[y][x] != 0:
            if start != 0 and board[y][x] != start and length >= 2:
                end = board[y][x]
                if dist[start][end] > length:
                    dist[start][end] = length
                    dist[end][start] = length

            start = board[y][x]
            length = 0

        else:
            if start != 0:
                length += 1

# 3. 열 스캔
for x in range(m):
    start = 0
    length = 0

    for y in range(n):
        if board[y][x] != 0:
            if start != 0 and board[y][x] != start and length >= 2:
                end = board[y][x]
                if dist[start][end] > length:
                    dist[start][end] = length
                    dist[end][start] = length

            start = board[y][x]
            length = 0

        else:
            if start != 0:
                length += 1

edges = []
for i in range(2, island_idx):
    for j in range(i + 1, island_idx):
        if dist[i][j] != INF:
            edges.append((dist[i][j], i, j))

# 4. 크루스칼
parent = [i for i in range(island_idx)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parent[b] = a
    return True

edges.sort()

total = 0
used = 0

for cost, a, b in edges:
    if union(a, b):
        total += cost
        used += 1

if used == island_count - 1:
    print(total)
else:
    print(-1)