import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = list(map(int, input().split()))
nlist.sort()

for perm in permutations(nlist, m):
    for i in perm:
        print(i, end=" ")
    print()