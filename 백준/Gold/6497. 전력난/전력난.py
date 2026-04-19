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

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    parent = [0] * (n)

    for i in range(n):
        parent[i] = i

    edges = []
    total = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        total += c

    edges.sort()

    result = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            result += cost
            union_parent(parent, a, b)

    print(total - result)