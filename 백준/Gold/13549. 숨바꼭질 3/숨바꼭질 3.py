from collections import deque

INF = 1_000_000
n, k = map(int, input().split())
visited = [INF] * 100_001
visited[n] = 0

def move(i, now):
    if i == 0:
        return now * 2
    elif i == 1:
        return now - 1
    elif i == 2:
        return now + 1

def bfs(start, k):
    queue = deque([(start, 0)])

    while queue:
        now, time = queue.popleft()

        if now == k:
            return visited[now]

        for i in range(3):
            temp = move(i, now)
            if 0 <= temp <= 100_000 and visited[temp] == INF:
                if i == 0:
                    visited[temp] = time
                    queue.appendleft((temp, visited[temp]))
                else:
                    visited[temp] = time + 1
                    queue.append((temp, visited[temp]))

print(bfs(n, k))