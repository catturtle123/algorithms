import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(start):
    queue = deque([start])

    while queue:
        y, x, length = queue.popleft()

        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x

            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    if nlist[ny][nx] == 1:
                        visited[ny][nx] = True
                        nlist[ny][nx] = length + 1
                        queue.append((ny, nx, length + 1))


n, m = map(int, input().split())

nlist = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    nlist.append(list(map(int, input().split())))

is_break = False
for i in range(n):
    for j in range(m):
        if nlist[i][j] == 2:
            visited[i][j] = True
            nlist[i][j] = 0
            bfs((i, j, 0))
            is_break = True
            break
    
    if is_break:
        break

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            print(nlist[i][j], end=" ")
        else:
            if nlist[i][j] == 1:
                print(-1, end=" ")
            else:
                print(0, end=" ")
    print()