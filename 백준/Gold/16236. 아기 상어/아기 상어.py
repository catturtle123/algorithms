import sys, heapq
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start):
    global size

    min_dist = sys.maxsize
    queue = deque([start])
    
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        y, x, length = queue.popleft()

        if min_dist < length:
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0<= nx < n:
                if not visited[ny][nx]:

                    if maps[ny][nx] == 0:
                        visited[ny][nx] = True
                        queue.append((ny, nx, length + 1))

                    elif shark_size > maps[ny][nx]:
                        visited[ny][nx] = True
                        heapq.heappush(temp_result, (length + 1, ny, nx))

                        min_dist = length + 1

                        size += 1

                    elif shark_size == maps[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx, length + 1))
                    
                    else:
                        visited[ny][nx] = True

n = int(input())

maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))

stop_point = False
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            y = i
            x = j

            stop_point = True
            break
    
    if stop_point:
        break

shark_size = 2
feeding_size = 0
result = 0

temp_result = []
heapq.heapify(temp_result)
while True:
    size = 0
    temp_result.clear()

    bfs((y, x, 0))
    
    if size != 0:
        maps[y][x] = 0

        length, y, x = heapq.heappop(temp_result)

        maps[y][x] = 9
        result += length
        feeding_size += 1

        if feeding_size == shark_size:
            shark_size += 1
            feeding_size = 0
    else:
        break

print(result)