n = int(input())

nlist = []
for i in range(n):
    num = input()
    nlist.append(num)

nlist = set(nlist)
nlist = list(nlist)

nlist.sort()

ulist = []
count = 0
for i in range(1,51):
    for j in nlist:
        if i == len(j):
            ulist.append(j)
            count += 1
    if count == n:
        break


for i in ulist:
    print(i)