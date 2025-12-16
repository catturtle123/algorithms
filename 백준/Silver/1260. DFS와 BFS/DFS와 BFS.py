from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(v):
    print(v, end=" ")
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

def bfs(v):
    queue = deque([])
    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n + 1)
dfs(v)

print()

visited = [False] * (n + 1)
bfs(v)