import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * (n) for _ in range(m)]

    for i in range(k):
        a, b = map(int, input().split())
        maps[a][b] = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    count = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                count += 1
                queue = deque([(i, j)])
                maps[i][j] = 2

                while queue:
                    y, x = queue.popleft()

                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]

                        if 0 <= ny < m and 0 <= nx < n:
                            if maps[ny][nx] == 1:
                                maps[ny][nx] = 2
                                queue.append((ny, nx))

    print(count)