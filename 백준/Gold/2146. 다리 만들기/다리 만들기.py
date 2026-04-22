import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs_label(sy, sx, idx):
    q = deque()
    q.append((sy, sx))
    board[sy][sx] = idx

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 1:
                board[ny][nx] = idx
                q.append((ny, nx))

# 1. 섬 번호 매기기
island_idx = 2
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            bfs_label(y, x, island_idx)
            island_idx += 1

# 2. 멀티 소스 BFS 준비
owner = [[0] * n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]
q = deque()

for y in range(n):
    for x in range(n):
        if board[y][x] != 0:
            owner[y][x] = board[y][x]
            dist[y][x] = 0
            q.append((y, x))

# 3. 동시에 확장
answer = sys.maxsize

while q:
    y, x = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            # 아직 아무 섬도 오지 않은 칸이면 확장
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                owner[ny][nx] = owner[y][x]
                q.append((ny, nx))

            # 다른 섬/다른 확장 영역과 만난 경우
            elif owner[ny][nx] != owner[y][x]:
                answer = min(answer, dist[ny][nx] + dist[y][x])

print(answer)