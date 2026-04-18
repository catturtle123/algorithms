import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize

test = int(input())

def dikstra(start, graph, n):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if dist > distance[node]:
            continue

        for next_node, cost in graph[node]:
            new_dist = dist + cost
            if distance[next_node] > new_dist:
                heapq.heappush(queue, (new_dist, next_node))
                distance[next_node] = new_dist

    return distance

for _ in range(test):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    gh_dist = 0

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

        if (a == g and b == h) or (a == h and b == g):
            gh_dist = d

    destination_list = []
    for _ in range(t):
        a = int(input())
        destination_list.append(a)

    dist_s = dikstra(s, graph, n)
    dist_g = dikstra(g, graph, n)
    dist_h = dikstra(h, graph, n)

    result = []
    for des in destination_list:
        path1 = dist_s[g] + gh_dist + dist_h[des]
        path2 = dist_s[h] + gh_dist + dist_g[des]

        if dist_s[des] == path1 or dist_s[des] == path2:
            result.append(des)

    result.sort()
    print(*result)