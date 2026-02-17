nlist = list(map(int, input().split()))
mlist = list(map(int, input().split()))

nx = sum(nlist)
mx = sum(mlist)
if nx > mx:
    print(nx)
else:
    print(mx)