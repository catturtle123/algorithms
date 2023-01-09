a,b = map(int,input().split())

map1 = {}
for i in range(a):
    n = input()
    map1[n] = 1

nlist = []
for i in range(b):
    n = input()
    nlist.append(n)

for i in nlist:
    if i in map1:
        map1[i] += 1

nlist = []
for i in map1:
    if map1[i] > 1:
        nlist.append(i)

print(len(nlist))
nlist.sort()
for i in nlist:
    print(i)