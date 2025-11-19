import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

def dikstra(start_node):
    values = [INF] * (v + 1)

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

    return values

t = int(input())

for i in range(t):
    v, e, x = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for i in range(e):
        a, b, c = map(int, input().split())

        graph[b].append((c, a))

    computers_values = dikstra(x)

    result1 = 0
    result2 = 0
    for i in range(1, v + 1):
        if computers_values[i] != INF:
            result1 += 1
            result2 = max(result2, computers_values[i])
    
    print(result1, result2)