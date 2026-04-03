import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, visited, index):
    visited[index] = True
    print(index, end=" ")

    for i in graph[index]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for v in graph[vertex]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (n + 1)
dfs(graph, visited, start)
print()
visited = [False] * (n + 1)
bfs(graph, visited, start)