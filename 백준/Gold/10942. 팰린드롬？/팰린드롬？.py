import sys
n = int(input())
nlist = list(map(int, sys.stdin.readline().rstrip().split(' ')))
olist = [[1] * n for _ in range(n)]

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if nlist[i] != nlist[j] or olist[i + 1][j - 1] == 0:
            olist[i][j] = 0



r = int(input())
for i in range(r):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(olist[a - 1][b - 1])