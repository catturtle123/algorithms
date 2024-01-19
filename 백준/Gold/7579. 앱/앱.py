n, m = map(int,input().split(' '))
nlist = list(map(int,input().split(' ')))
mlist = list(map(int,input().split(' ')))
ulist = []
olist = [[0] * 10_001 for _ in range(len(nlist))]
count = 0

for i in range(len(nlist)):
    ulist.append((nlist[i], mlist[i]))

ulist.sort()
nlist = []
mlist = []

for i in ulist:
    nlist.append(i[0])
    mlist.append(i[1])
ulist.clear()

for i in range(mlist[0], 10_001):
    olist[0][i] = nlist[0]
count += mlist[0]

for i in range(1, len(nlist)):
    for j in range(10_001):
        if mlist[i] > j:
            olist[i][j] = olist[i - 1][j]
        else:
            olist[i][j] = max(olist[i - 1][j], olist[i - 1][j - mlist[i]] + nlist[i])

stop = False
for i in range(0, 10_001):
    for j in range(n):
        if m <= olist[j][i]:
            print(i)
            stop = True
            break
    if stop:
        break
