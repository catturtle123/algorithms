import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.insert(0, 0)
for i in range(1, len(nlist)):
    nlist[i] = nlist[i] + nlist[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(nlist[j] - nlist[i - 1])