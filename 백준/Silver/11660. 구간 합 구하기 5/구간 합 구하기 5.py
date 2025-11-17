import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nlist = []
nlist.append([0] * (n + 1))
for i in range(n):
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    nlist.append(temp)

for i in range(2, n + 1):
    nlist[1][i] += nlist[1][i - 1]
    nlist[i][1] += nlist[i - 1][1]

for i in range(2, n + 1):
    for j in range(2, n + 1):
        nlist[i][j] = nlist[i - 1][j] + nlist[i][j - 1] - nlist[i - 1][j - 1] + nlist[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    print(nlist[x2][y2] - nlist[x1 - 1][y2] - nlist[x2][y1 - 1] + nlist[x1 - 1][y1 - 1])