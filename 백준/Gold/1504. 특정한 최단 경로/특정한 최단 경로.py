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

node1, node2 = map(int, input().split())

# 시작 노드 -> 노드1
start_node = 1
end_node = node1

values = [INF] * (v + 1)
dikstra(start_node)

result1 = values[end_node]

# 노드1 -> 노드 2
start_node = node1
end_node = node2

values = [INF] * (v + 1)
dikstra(start_node)

result2 = values[end_node]

# 노드 2 -> 마지막 노드
start_node = node2
end_node = v

values = [INF] * (v + 1)
dikstra(start_node)

result3 = values[end_node]

# 시작 노드 -> 노드2
start_node = 1
end_node = node2

values = [INF] * (v + 1)
dikstra(start_node)

result4 = values[end_node]

# 노드2 -> 노드 1
start_node = node2
end_node = node1

values = [INF] * (v + 1)
dikstra(start_node)

result5 = values[end_node]

# 노드 1 -> 마지막 노드
start_node = node1
end_node = v

values = [INF] * (v + 1)
dikstra(start_node)

result6 = values[end_node]

result = min(result1 + result2 + result3, result4 + result5 + result6)
if result >= INF:
    print(-1)
else:
    print(result)