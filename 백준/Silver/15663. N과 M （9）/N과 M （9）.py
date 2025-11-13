from itertools import permutations

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

result = set()
for comb in permutations(nlist, m):
    result.add(comb)

result = list(result)
result.sort()

for i in result:
    for j in i:
        print(j, end=" ")
    print()