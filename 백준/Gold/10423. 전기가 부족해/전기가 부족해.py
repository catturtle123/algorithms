import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

electric_list = list(map(int, input().split()))

edges = []
for _ in range(m):
    a, b ,c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for i in range(1, k):
    union_parent(parent, electric_list[0], electric_list[i])

result = 0
for cost, a, b in edges:
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a != parent_b:
        result += cost
        union_parent(parent, a, b)

print(result)