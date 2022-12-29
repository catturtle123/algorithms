n = int(input())

nlist = []
for i in range(n):
    ulist = []
    ulist = list(map(int,input().split()))
    nlist += ulist

klist = []
for i in range(n):
    klist.append(1)

count = 0
for i in range(0,len(nlist),2):
    for j in range(0,len(nlist),2):
        if nlist[i] < nlist[j] and nlist[i+1] < nlist[j+1]:
            klist[count] += 1
    count += 1



for i in klist:
    print(i,end=" ")
