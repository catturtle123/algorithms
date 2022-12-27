nlist = list(map(int,input().split()))

alist = [1,2,3,4,5,6,7,8]
dlist = [8,7,6,5,4,3,2,1]

a = 0
d = 0

for i in range(8):
    if nlist[i] == alist[i]:
        a+=1
    
    if nlist[i] == dlist[i]:
        d+=1

if a == 8:
    print("ascending")
elif d == 8:
    print("descending")
else:
    print("mixed")