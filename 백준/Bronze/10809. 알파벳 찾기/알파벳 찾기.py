n = input()

nlist = []

for i in range(26):
    nlist.append(-1)

for i in n:
    c = ord(i) - 97
    nlist[c] = n.find(i)

for i in nlist:
    print(i,end=" ")
