import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([(start, 0)])

    max_value = -1
    max_node = -1
    while queue:
        node, cost = queue.popleft()

        if max_value < cost:
            max_value = cost
            max_node = node

        for i in graph[node]:
            if not visited[i[0]]:
                queue.append((i[0], cost + i[1]))
                visited[i[0]] = True

    return max_node, max_value

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n):
    nlist = list(map(int, input().split()))
    o = nlist[0]
    for j in range(1, len(nlist) - 2, 2):
        a, b = nlist[j], nlist[j + 1]
        graph[o].append((a, b))

visited = [False] * (n + 1)
visited[1] = True
node, value = bfs(1)

visited = [False] * (n + 1)
visited[node] = True
node, value = bfs(node)
print(value)
