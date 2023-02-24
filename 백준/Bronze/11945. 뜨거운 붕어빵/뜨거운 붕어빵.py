a,b = map(int,input().split())

for i in range(a):
    nlist = []
    n = input()
    for i in n:
        nlist.append(i)
    for i in range(len(n)//2):
        nlist[i],nlist[len(n)-i-1] =  nlist[len(n)-i-1] ,nlist[i]
    for i in nlist:
        print(i,end="")
    print()