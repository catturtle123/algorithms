# N x M 크기의 미로
# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# 1, 1에서 출발, N, M까지의 최소 칸수를 구하시오.
# 입력 : N, M / 미로
# 출력 : 최소의 칸 수
# BFS

import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(maps):
    queue = deque([(0, 0, 1)])
    maps[0][0] = 0

    while queue:
        y, x, value = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                if ny == n - 1 and nx == m - 1:
                    return value
                queue.append((ny, nx, value + 1))
                maps[ny][nx] = 0

n, m = map(int, input().split())

maps = []
for _ in range(n):
    s = input().rstrip()
    temp = []
    for i in s:
        temp.append(int(i))
    maps.append(temp)

print(bfs(maps) + 1)