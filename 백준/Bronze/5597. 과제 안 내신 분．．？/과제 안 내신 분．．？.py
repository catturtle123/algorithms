nlist = []
for i in range(28):
    n = int(input())
    nlist.append(n)

nlist.sort()
nlist = set(nlist)

ulist = []
for i in range(30):
    ulist.append(i+1)
ulist = set(ulist)

slist = ulist - nlist

slist = list(slist)
slist.sort()

for i in slist:
    print(i)