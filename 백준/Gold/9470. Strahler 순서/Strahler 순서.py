import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    in_degree = [0] * (m + 1)
    order = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    queue = deque([])
    for i in range(1, m + 1):
        if in_degree[i] == 0:
            order[i] = 1
            queue.append(i)

    temp = [[] for _ in range(m + 1)]
    while queue:
        node = queue.popleft()

        if len(temp[node]) == 1:
            order[node] = temp[node][0]
        elif len(temp[node]) > 1:
            temp[node].sort()
            if temp[node][-2] == temp[node][-1]:
                order[node] = max(temp[node]) + 1
            else:
                order[node] = temp[node][-1]

        for i in graph[node]:
            temp[i].append(order[node])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    print(k, order[m])