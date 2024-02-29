c, n = map(int, input().split(' '))

nlist = []
nlist.append((0,0))
for i in range(n):
    a, b = map(int, input().split(' '))
    nlist.append((a, b))

rlist = [[0] * 100_001 for _ in range(n + 1)]
nlist.sort()

for i in range(1, n + 1):
    for j in range(len(rlist[i])):
        if j < nlist[i][0]:
            rlist[i][j] = rlist[i - 1][j]
        else:
            rlist[i][j] = max(rlist[i - 1][j - nlist[i][0]] + nlist[i][1], nlist[i][1] + rlist[i][j - nlist[i][0]], rlist[i - 1][j])

isfinish = False
for i in range(100_001):
    for j in range(n + 1):
        if rlist[j][i] >= c:
            print(i)
            isfinish = True
            break
    if isfinish:
        break


