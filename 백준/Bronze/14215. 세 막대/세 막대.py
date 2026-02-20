nlist = list(map(int, input().split()))

nlist.sort()

if nlist[2] >= nlist[0] + nlist[1]:
    nlist[2] = nlist[0] + nlist[1] - 1

print(sum(nlist))