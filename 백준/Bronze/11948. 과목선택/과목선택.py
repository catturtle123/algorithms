
nlist1 = []
for _ in range(4):
    n = int(input())
    nlist1.append(n)

nlist2 = []
for _ in range(2):
    n = int(input())
    nlist2.append(n)


nlist1.sort(reverse=True)
nlist2.sort(reverse=True)

print(sum(nlist1[:3]) + nlist2[0])