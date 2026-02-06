nlist = []
for _ in range(5):
    n = int(input())
    nlist.append(n)

s = max(nlist[1] / nlist[3], nlist[2] / nlist[4])

print(int(nlist[0] - s))