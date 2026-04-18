import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize
n, m = map(int, input().split())
see_list = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

distance = [INF] * n

def dikstra(start):
    queue = []
    queue.append((0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if dist > distance[node]:
            continue

        for i in graph[node]:
            if (i[0] == n - 1 or see_list[i[0]] != 1) and distance[i[0]] > dist + i[1]:
                heapq.heappush(queue, (dist + i[1], i[0]))
                distance[i[0]] = dist + i[1]


dikstra(0)
if distance[n - 1] == INF:
    print(-1)
else:
    print(distance[n - 1])