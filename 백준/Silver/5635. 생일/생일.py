nlist = []
n = int(input())

for i in range(n):
    a,b,c,d = map(str,input().split())
    nlist.append([a,int(b),int(c),int(d)])


for i in range(n-1,0,-1):
    for j in range(i):
        if nlist[j][3] > nlist[j+1][3]:
            nlist[j+1],nlist[j] = nlist[j],nlist[j+1]

for i in range(n-1,0,-1):
    for j in range(i):
        if (nlist[j][2] > nlist[j+1][2]) and (nlist[j][3] == nlist[j+1][3]):
            nlist[j+1],nlist[j] = nlist[j],nlist[j+1]

for i in range(n-1,0,-1):
    for j in range(i):
        if (nlist[j][1] > nlist[j+1][1]) and (nlist[j][1] == nlist[j+1][1]):
            nlist[j+1],nlist[j] = nlist[j],nlist[j+1]

print(f"{nlist[-1][0]}\n{nlist[0][0]}")