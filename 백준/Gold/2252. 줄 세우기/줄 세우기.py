import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = deque([])
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] <= 0:
            queue.append(i)