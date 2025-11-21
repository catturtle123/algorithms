from collections import deque

INF = 1_000_000
n, k = map(int, input().split())
visited = [INF] * 100_001
visited[n] = 0

def move(i, now):
    if i == 0:
        return now * 2
    elif i == 1:
        return now + 1
    elif i == 2:
        return now - 1

def bfs(start, k):
    queue = deque([(start, 0)])

    while queue:
        now, time = queue.popleft()

        for i in range(3):
            temp = move(i, now)
            if 0 <= temp <= 100_000:
                if i == 0 and visited[temp] > visited[now]:
                    visited[temp] = time
                    queue.appendleft((temp, visited[temp]))
                else:
                    if visited[temp] > visited[now] + 1:
                        visited[temp] = time + 1
                        queue.append((temp, visited[temp]))

    return visited[k]

print(bfs(n, k))