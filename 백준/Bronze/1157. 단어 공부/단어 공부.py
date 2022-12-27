a = input()

smallStr = "qwertyuiopasdfghjklzxcvbnm"
bigStr = "QWERTYUIOPASDFGHJKLZXCVBNM"

nlist = []
for i in smallStr:
    nlist.append(a.count(i))

for i in bigStr:
    u = a.count(i)
    h = bigStr.find(i)
    nlist[h] += u



for i in range(len(nlist)):
    if max(nlist) == nlist[i]:
        p = i
        break

nlist.sort()    

if nlist[-1] == nlist[-2]:
    print("?")
else:
    print(bigStr[p])

