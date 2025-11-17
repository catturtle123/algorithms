from itertools import combinations_with_replacement

n, m = map(int, input().split())

nlist = list(map(int, input().split()))

nlist.sort()

result = set()
for comb in combinations_with_replacement(nlist, m):
    result.add(comb)

result = list(result)
result.sort()

for i in result:
    for j in i:
        print(j, end=" ")
    print()