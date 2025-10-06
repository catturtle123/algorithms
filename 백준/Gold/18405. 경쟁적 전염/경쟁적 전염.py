import sys
from collections import deque
import copy

input = sys.stdin.readline

N, K = map(int, input().split(" "))

maps = []
virous = []
for i in range(N):
    maps.append(list(map(int, input().split(" "))))

for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            virous.append((maps[i][j], i, j))

S, X, Y = map(int, input().split(" "))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


# BFS
def bfs(start): # y, x
    temp = []
    queue = deque(start)

    while queue:
        q = queue.popleft()
        
        for i in range(4):
            ny, nx = q[1] + dy[i], q[2] + dx[i]

            if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] == 0:
                maps[ny][nx] = q[0] 
                temp.append((q[0], ny, nx))

    return temp

for time in range(S):
    # virous 
    virous.sort()
    virous = copy.deepcopy(bfs(virous))

print(maps[X - 1][Y - 1])