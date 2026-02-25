from collections import deque
import sys
input = sys.stdin.readline

v, e, s = map(int, input().split())

graph = [[] for _ in range(v + 1)]

def dfs(x):
    print(x, end=" ")
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        s = queue.popleft()

        print(s, end=" ")

        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for i in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)
    
for g in graph:
    g.sort()

visited = [False] * (v + 1)
dfs(s)

print()

visited = [False] * (v + 1)
bfs(s)