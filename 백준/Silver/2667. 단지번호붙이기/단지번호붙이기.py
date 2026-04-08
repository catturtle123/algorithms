# 5 < n < 25
# 세대수 정하기

import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(maps, start):
    queue = deque([start])
    maps[start[0]][start[1]] = 0

    result = 0
    while queue:
        y, x = queue.popleft()
    
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] == 1:
                result += 1
                maps[ny][nx] = 0
                queue.append((ny, nx))
    
    return result + 1

n = int(input())
maps = []
for _ in range(n):
    s = input().rstrip()
    temp = []
    for i in s:
        temp.append(int(i))
    maps.append(temp)

result_list = []
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            temp = bfs(maps, (i, j))

            if temp != 0:
                result_list.append(temp)

print(len(result_list))
result_list.sort()
for i in result_list:
    print(i)