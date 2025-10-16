import sys

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

input = sys.stdin.readline

n = int(input())

planets = []
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    planets.append((a, b, c, i))

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
planets = sorted(planets, key= lambda x : x[0])
for i in range(1, len(planets)):
    cost = min(abs(planets[i - 1][0] - planets[i][0]), abs(planets[i - 1][1] - planets[i][1]), abs(planets[i - 1][2] - planets[i][2]))
    edges.append((cost, planets[i - 1][3], planets[i][3]))

planets = sorted(planets, key= lambda x : x[1])
for i in range(1, len(planets)):
    cost = min(abs(planets[i - 1][0] - planets[i][0]), abs(planets[i - 1][1] - planets[i][1]), abs(planets[i - 1][2] - planets[i][2]))
    edges.append((cost, planets[i - 1][3], planets[i][3]))

planets = sorted(planets, key= lambda x : x[2])
for i in range(1, len(planets)):
    cost = min(abs(planets[i - 1][0] - planets[i][0]), abs(planets[i - 1][1] - planets[i][1]), abs(planets[i - 1][2] - planets[i][2]))
    edges.append((cost, planets[i - 1][3], planets[i][3]))

edges.sort()

result = 0
for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])
        result += edge[0]

print(result)