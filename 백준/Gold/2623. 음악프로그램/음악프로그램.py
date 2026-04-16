import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    nlist = list(map(int, input().split()))

    for i in range(2, len(nlist)):
        graph[nlist[i - 1]].append(nlist[i])
        in_degree[nlist[i]] += 1

queue = deque([])
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

result_list = []

while queue:
    node = queue.popleft()
    result_list.append(node)

    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] <= 0:
            queue.append(i)

if len(result_list) != n:
    print(0)
else:
    for i in result_list:
        print(i)