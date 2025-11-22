import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    result = 0
    result_node = 0
    while queue:
        node, total = queue.popleft()

        if total > result:
            result = total
            result_node = node

        for i in tree[node]:
            if not visited[i[0]]:
                queue.append((i[0], total + i[1]))
                visited[i[0]] = True

    return result, result_node

n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

t = 0
edge_node_value1, edge_node1 = bfs(1)
edge_node_value2, edge_node2 = bfs(edge_node1)

print(edge_node_value2)