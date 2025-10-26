import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        q = queue.popleft()

        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1
    
print(count)