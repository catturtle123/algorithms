import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

def dikstra(start_node):
    queue = []
    values[start_node] = 0

    heapq.heapify(queue)
    heapq.heappush(queue, (0, start_node))

    while queue:
        value, node = heapq.heappop(queue)
        if values[node] < value:
            continue

        for i in graph[node]:
            if values[i[1]] > value + i[0]:
                    values[i[1]] = value + i[0]
                    heapq.heappush(queue, (i[0] + value, i[1]))

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for i in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((c, b))
    graph[b].append((c, a))

start_node, end_node = map(int, input().split())

values = [INF] * (v + 1)
dikstra(start_node)

print(values[end_node])