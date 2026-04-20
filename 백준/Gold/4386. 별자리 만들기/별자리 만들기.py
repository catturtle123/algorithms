import sys, math
from itertools import combinations
input = sys.stdin.readline

n = int(input())

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

parent = [0] * (n)

for i in range(n):
    parent[i] = i

y_x = []
for _ in range(n):
    a, b = map(float, input().split())
    y_x.append((a, b))

edges = []
for comb in combinations(range(len(y_x)), 2):
    a = comb[0]
    b = comb[1]

    a_y, a_x = y_x[a][0], y_x[a][1]
    b_y, b_x = y_x[b][0], y_x[b][1]
    length = math.sqrt(pow(a_y - b_y, 2) + pow(a_x - b_x, 2))

    edges.append((length, a, b))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(f"{result:.2f}")