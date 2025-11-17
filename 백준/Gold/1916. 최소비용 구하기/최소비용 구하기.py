import sys
import heapq
input = sys.stdin.readline

def dikstra(start):
    queue = [(start, 0)]
    heapq.heapify(queue)

    while queue:
        node, value = heapq.heappop(queue)

        if values[node] < value:
            continue

        for i in graph[node]:
            if values[i[0]] > i[1] + value:
                values[i[0]] = i[1] + value
                heapq.heappush(queue, (i[0], i[1] + value))

n = int(input())
m = int(input())

values = [sys.maxsize] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


start, end = map(int, input().split())

dikstra(start)

print(values[end])