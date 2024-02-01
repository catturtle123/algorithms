n = input()
nlist = list(map(int, input().split(' ')))
nlist.sort()

sum = 0
for i in range(len(nlist)):
    if nlist[0] > 1:
        print(1)
        break
    sum += nlist[i]
    if i == len(nlist) - 1:
        print(sum + 1)
        break
    if sum + 1 < nlist[i + 1]:
        print(sum + 1)
        break
        