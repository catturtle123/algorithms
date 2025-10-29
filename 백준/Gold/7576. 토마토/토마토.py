import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
queue = deque([])

def bfs(start):


    while start:
        y, x, time = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if nlist[ny][nx] == sys.maxsize:
                    nlist[ny][nx] = min(nlist[ny][nx], time + 1)
                    queue.append((ny, nx, time + 1))

    

nlist = []
for i in range(N):
    nlist.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if nlist[i][j] == 1:
            queue.append((i, j, 0))
            nlist[i][j] = 0

        elif nlist[i][j] == 0:
            nlist[i][j] = sys.maxsize

bfs(queue)

max_time = 0
is_break = False
for i in range(N):
    for j in range(M):
        if nlist[i][j] == sys.maxsize:
            print(-1)
            is_break = True
            break
        
        # if nlist[i][j] == 0:
        #     print(0)
        #     is_break = True
        #     break
        

        max_time = max(nlist[i][j], max_time)

    if is_break:
        break

if not is_break:
    print(max_time)