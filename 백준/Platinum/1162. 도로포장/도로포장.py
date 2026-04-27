import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [[INF] * (k + 1) for _ in range(n + 1)]

queue = []
heapq.heappush(queue, (0, 1, 0))
distance[1][0] = 0

while queue:
    dist, node, cnt = heapq.heappop(queue)

    if distance[node][cnt] < dist:
        continue

    for next_node, cost in graph[node]:
        # 1. 포장하지 않고 이동
        if distance[next_node][cnt] > dist + cost:
            distance[next_node][cnt] = dist + cost
            heapq.heappush(queue, (dist + cost, next_node, cnt))

        # 2. 포장하고 이동
        if cnt < k and distance[next_node][cnt + 1] > dist:
            distance[next_node][cnt + 1] = dist
            heapq.heappush(queue, (dist, next_node, cnt + 1))

print(min(distance[n]))