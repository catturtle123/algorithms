n = input()
nlist = []

for i in range(26):
    nlist.append(0)

for i in n:
    u = ord(i) - 97
    nlist[u] += 1

for i in nlist:
    print(i)