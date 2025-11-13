import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    result = []
    queue = deque([(1, 0)])

    while queue:
        node, parent = queue.popleft()

        result.append((node, parent))

        for i in graph[node]:
            if not visited[i]:
                queue.append((i, node))
                visited[i] = True

    return result

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = bfs()
result.sort()

for i in range(2, len(result)):
    print(result[i][1])