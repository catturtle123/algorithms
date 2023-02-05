n = int(input())

for i in range(n):
    nlist = list(map(int,input().split()))
    nlist = nlist[1:]
    n = len(nlist)
    s = sum(nlist)
    a = s/n
    
    slist = []
    for j in nlist:
        if a < j:
            slist.append(j)
    
    f = float((len(slist)/n)*100)
    
    print("%.3f" %(f),end="")
    print("%")