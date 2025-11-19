import sys
import heapq
import copy
input = sys.stdin.readline

INF = sys.maxsize

def dikstra(start_node):
    values = [INF] * (v + 1)

    queue = []
    node_list = [start_node]
    values[start_node] = 0

    heapq.heapify(queue)
    heapq.heappush(queue, (0, start_node, node_list))

    while queue:
        value, node, nodes = heapq.heappop(queue)
        
        if values[node] < value:
            continue

        for i in graph[node]:
            if values[i[1]] > value + i[0]:
                values[i[1]] = value + i[0]

                temp = copy.deepcopy(nodes)
                temp.append(i[1])

                if i[1] == end_node:
                    result = temp

                heapq.heappush(queue, (i[0] + value, i[1], temp))

    return values, result

v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]

for i in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((c, b))

start_node, end_node = map(int, input().split())

values, result = dikstra(start_node)

print(values[end_node])
print(len(result))
for i in result:
    print(i, end=" ")