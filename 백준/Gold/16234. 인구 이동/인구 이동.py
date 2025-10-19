import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split()) # 맵의 칸수, 최소, 최대

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

def bfs(start):
    visited[start[0]][start[1]] = True
    queue = deque([start])
    result = []
    
    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]
        population = maps[y][x]
        result.append((y, x, population))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i] 

            if 0 <= ny < n and 0 <= nx < n:
                next_population = maps[ny][nx]

                if l <= abs(next_population - population) <= r:
                    if not visited[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                        
    return result

count = 0
while True:
    all_result = []
    visited = [[False] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                result = bfs((i, j))
                all_result.append(result)

    for i in all_result:
        temp_result = i

        sums = 0
        for j in temp_result:
            sums += j[2]

        average = sums // len(temp_result)
        for j in temp_result:
            maps[j[0]][j[1]] = average

    if len(all_result) == (n * n):
        break
    else:
        count += 1

print(count)