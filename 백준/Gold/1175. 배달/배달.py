import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

c_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'C':
            c_list.append((i, j))

c1x, c1y = c_list[0]
c2x, c2y = c_list[1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
queue = deque()

for d in range(4):
    visited[sx][sy][0][d] = True
queue.append((sx, sy, 0, -1, 0))  # x, y, delivered, last_dir, dist

while queue:
    x, y, delivered, last_dir, dist = queue.popleft()

    if delivered == 3:
        print(dist)
        exit()

    for nd in range(4):
        if nd == last_dir:
            continue

        nx = x + dx[nd]
        ny = y + dy[nd]

        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if board[nx][ny] == '#':
            continue

        ndelivered = delivered
        if (nx, ny) == (c1x, c1y):
            ndelivered |= 1
        if (nx, ny) == (c2x, c2y):
            ndelivered |= 2

        if not visited[nx][ny][ndelivered][nd]:
            visited[nx][ny][ndelivered][nd] = True
            queue.append((nx, ny, ndelivered, nd, dist + 1))

print(-1)