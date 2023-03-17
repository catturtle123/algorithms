a,b = map(int,input().split())

nlist = []
for i in range(a):
    s = list(map(int,input().split()))
    nlist.append(s)

nlist2 = []

for i in range(a):
    s = list(map(int,input().split()))
    nlist2.append(s)

nlist3 = []
for i in range(a):
    for j in range(b):
        nlist3.append(nlist[i][j] + nlist2[i][j])

count = 0
for i in nlist3:
    print(i,end=" ")
    count += 1
    if count % b == 0:
        print()