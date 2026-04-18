import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n = int(input())
board = []
for _ in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

def bfs(low, high):
    if not (low <= board[0][0] <= high):
        return False
    if not (low <= board[n - 1][n - 1] <= high):
        return False
    
    visited = [[False] * n for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        y, x = queue.popleft()

        if y == n - 1 and x == n - 1:
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if low <= board[ny][nx] <= high:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    
    return False

answer = 200
low = 0
high = 0

while low <= 200 and high <= 200:
    if bfs(low, high):
        answer = min(answer, high - low)
        low += 1
    else:
        high += 1

print(answer)
