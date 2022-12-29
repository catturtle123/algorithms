while True:
    nlist = list(map(int,input().split()))
    if nlist[0] == 0 and nlist[1] == 0 and nlist[2] == 0:
        break
    nlist.sort()
    if nlist[0]**2 + nlist[1]**2 == nlist[2]**2:
        print("right")
    else:
        print("wrong")
