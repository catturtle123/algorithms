import sys
input = sys.stdin.readline
from collections import deque

m = int(input())
graph = [[] for _ in range(m + 1)]
in_degree = [0] * (m + 1)
time = [0] * (m + 1)

for i in range(1, m + 1):
    nlist = list(map(int, input().split()))
    time[i] = nlist[0]
    for pre in nlist[1:-1]:
        graph[pre].append(i)
        in_degree[i] += 1

queue = deque()
result = time[:]

for i in range(1, m + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    for i in graph[node]:
        result[i] = max(result[i], result[node] + time[i])
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)

for i in range(1, m + 1):
    print(result[i])