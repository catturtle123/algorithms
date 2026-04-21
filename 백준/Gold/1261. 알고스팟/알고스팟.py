import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

distance = [[sys.maxsize] * m for _ in range(n)]
distance[0][0] = 0

queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        cost = distance[x][y] + graph[nx][ny]

        if distance[nx][ny] > cost:
            distance[nx][ny] = cost

            if graph[nx][ny] == 0:
                queue.appendleft((nx, ny))
            else:
                queue.append((nx, ny))

print(distance[n - 1][m - 1])