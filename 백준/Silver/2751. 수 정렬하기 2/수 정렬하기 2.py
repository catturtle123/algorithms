n = int(input())

nlist = []
for i in range(n):
    num = int(input())
    nlist.append(num)

nlist.sort()

for i in nlist:
    print(i)