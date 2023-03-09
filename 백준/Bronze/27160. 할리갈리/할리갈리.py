n = int(input())

fmap = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}

for i in range(n):
    a,b = map(str,input().split())
    fmap[a] += int(b)


flist = []

for i in range(4):
    flist.append((list(fmap.keys())[i],list(fmap.values())[i]))

tf = 0
for i in flist:
    if i[1] == 5:
        print("YES")
        tf = 1
        break
 
if tf == 0:
    print("NO")