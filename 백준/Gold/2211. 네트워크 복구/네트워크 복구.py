import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

distance = [INF] * (n + 1)
distance_list = [[] for _ in range(n + 1)]

def dikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if dist > distance[node]:
            continue

        for i in graph[node]:
            if distance[i[0]] > dist + i[1]:
                heapq.heappush(queue, (dist + i[1], i[0]))
                distance[i[0]] = dist + i[1]
                distance_list[i[0]].append((node, i[0]))


dikstra(1)
result = []
for i in range(2, len(distance_list)):
    a = distance_list[i]
    result.append(a[-1])

print(len(result))
for i in result:
    print(i[0], i[1])