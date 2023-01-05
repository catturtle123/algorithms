n = int(input())

nlist = []
for i in range(n):
    a,b = map(int,input().split())
    nlist.append((a,b))

nlist.sort()

for i in range(n):
    print(f"{nlist[i][0]} {nlist[i][1]}")