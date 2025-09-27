import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split(" "))

nlist = []
for i in range(n):
    nlist.append(list(map(int, input().split())))

chicken_market = []
house = []
for i in range(n):
    for j in range(n):
        if nlist[i][j] == 2:
            chicken_market.append((i, j))
        if nlist[i][j] == 1:
            house.append((i, j))

length_list = []
for i in chicken_market:
    temp_list = []
    for j in house:
        length = abs(i[0] - j[0]) + abs(i[1] - j[1])
        temp_list.append(length)
    length_list.append(temp_list)

ans = float('inf')
for comb in combinations(range(len(chicken_market)), m):
    total = 0
    for h_idx in range(len(house)):
        dist = min(length_list[c_idx][h_idx] for c_idx in comb)
        total += dist
    ans = min(ans, total)

print(ans)