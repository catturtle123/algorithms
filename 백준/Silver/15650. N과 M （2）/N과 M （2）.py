import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = []
for i in range(1, n + 1):
    nlist.append(i)

rlist = []
for perm in permutations(nlist, m):
    if sorted(perm) in rlist:
        continue

    rlist.append(sorted(perm))

    for i in perm:
        print(i, end=" ")
    print()