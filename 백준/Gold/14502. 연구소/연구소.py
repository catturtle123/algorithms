import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split(" "))
maps = []
for i in range(n):
    maps.append(list(map(int, input().split(" "))))

virous = []
empty = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            virous.append((i, j))
        elif maps[i][j] == 0:
            empty.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
for comb in combinations(empty, 3):
    new_maps = copy.deepcopy(maps)

    # 벽 세우기
    for i in comb:
        new_maps[i[0]][i[1]] = 1
    
    # 바이러스 퍼트리기
    queue = deque(virous)

    while queue:
        q = queue.popleft()

        for i in range(4):
            ny, nx = q[0] + dy[i], q[1] + dx[i]

            if 0 <= ny < n and 0 <= nx < m and new_maps[ny][nx] == 0:   
                queue.append((ny, nx))
                new_maps[ny][nx] = 2
    
    # 0 갯수
    count = 0
    for i in range(n):
        for j in range(m):
            if new_maps[i][j] == 0:
                count += 1
    
    result = max(result, count)

print(result)