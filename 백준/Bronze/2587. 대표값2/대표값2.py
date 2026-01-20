nlist = []
for i in range(5):
    n = int(input())
    nlist.append(n)
    
nlist.sort()
print(sum(nlist) // 5)
print(nlist[2])