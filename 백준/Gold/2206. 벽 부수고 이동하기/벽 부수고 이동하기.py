import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
INF = sys.maxsize

def bfs():
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = True

    result = 1
    while queue:
        for _ in range(len(queue)):
            y, x, b = queue.popleft()

            if y == n - 1 and x == m - 1:
                return result

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx] == 0 and not visited[ny][nx][b]:
                        visited[ny][nx][b] = True
                        queue.append((ny, nx, b))
                    
                    if maps[ny][nx] == 1 and b == 0 and not visited[ny][nx][1]:
                        visited[ny][nx][1] = True
                        queue.append((ny, nx, 1))
            
        result += 1

    return -1

n, m = map(int, input().split())

maps = []

for i in range(n):
    s = input().rstrip()
    temp = []
    for j in s:
        temp.append(int(j))
    
    maps.append(temp)

print(bfs())