import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for h in range(2, 10):
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if board[i][j] < h:
                    visited[i][j] = True
                    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] < h:
                visited[nx][ny] = True
                queue.append((nx, ny))

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if board[i][j] < h and not visited[i][j]:
                result += 1

print(result)