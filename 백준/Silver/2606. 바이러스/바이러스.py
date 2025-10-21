import sys

n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(visited.count(True) - 1)