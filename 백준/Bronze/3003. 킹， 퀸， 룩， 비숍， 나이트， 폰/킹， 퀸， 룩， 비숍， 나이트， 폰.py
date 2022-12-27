clist = list(map(int,input().split()))
olist = [1,1,2,2,2,8]


for i in range(len(clist)):
    print(olist[i]-clist[i],end=" ") 