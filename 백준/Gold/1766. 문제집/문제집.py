import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

priority_queue = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        priority_queue.append(i)
heapq.heapify(priority_queue)

while priority_queue:
    w = heapq.heappop(priority_queue)
    print(w, end=" ")

    for i in graph[w]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(priority_queue, i)