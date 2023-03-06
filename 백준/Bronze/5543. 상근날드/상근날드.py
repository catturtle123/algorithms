nlist = []
blist = []

for i in range(3):
    nlist.append(int(input()))

for i in range(2):
    blist.append(int(input()))

print(min(nlist)+min(blist)-50)
