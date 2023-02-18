import sys
n = int(input())

nlist = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    nlist.append((a,b))

nlist = sorted(nlist,key=lambda x: (x[1],x[0]))

count = 1
end = nlist[0][1]
for j in nlist[1:]:
    if end <= j[0]:
        end = j[1]
        count += 1


print(count)