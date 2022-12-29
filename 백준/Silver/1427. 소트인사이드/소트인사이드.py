n = input()


nlist = []
for i in n:
    nlist.append(i)

ulist = []
for i in nlist:
    ulist.append(int(i))



ulist.sort()
ulist.reverse()

for i in ulist:
    print(i,end="")