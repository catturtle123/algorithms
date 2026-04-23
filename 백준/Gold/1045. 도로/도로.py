import sys
input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return 0
    parent[b] = a
    return 1

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

road_list = []
for i in range(n):
    for j in range(i + 1, n):
        if board[i][j] == 'Y':
            road_list.append((i, j))

result_list = []
count_list = [0] * n
road_count = len(road_list)

for i in range(road_count):
    if len(result_list) == m:
        break

    a, b = road_list[i]

    temp_list = result_list[:]
    temp_list.append((a, b))

    parent = [i for i in range(n)]
    group_count = n
    for x, y in temp_list:
        group_count -= union(parent, x, y)

    total_count = len(temp_list) + (road_count - i - 1)
    if total_count < m:
        continue

    if len(temp_list) + (group_count - 1) > m:
        continue

    parent2 = parent[:]
    group_count2 = group_count

    for j in range(i + 1, road_count):
        x, y = road_list[j]
        group_count2 -= union(parent2, x, y)

    if group_count2 == 1:
        result_list.append((a, b))
        count_list[a] += 1
        count_list[b] += 1

if len(result_list) != m:
    print(-1)
    exit()

parent = [i for i in range(n)]
group_count = n
for a, b in result_list:
    group_count -= union(parent, a, b)

if group_count != 1:
    print(-1)
else:
    print(*count_list)