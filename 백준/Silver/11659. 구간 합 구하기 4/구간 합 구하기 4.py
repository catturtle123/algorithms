import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.insert(0, 0)
for i in range(2, len(nlist)):
    nlist[i] += nlist[i - 1]

for i in range(m):
    a, b = map(int, input().split())

    print(nlist[b] - nlist[a - 1])