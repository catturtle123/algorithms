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

n = int(input())

edges = []
for i in range(1, n + 1):
    m = int(input())
    edges.append((m, 0, i))

temp_list = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp_list.append(temp)

for i in range(n):
    for j in range(n):
        edges.append((temp_list[i][j], i + 1, j + 1))

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

edges.sort()
result = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)