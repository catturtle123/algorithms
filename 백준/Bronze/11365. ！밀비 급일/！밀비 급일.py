while True:
    n = input()

    if n == "END":
        break

    nlist = [i for i in n]

    for i in range(len(nlist)//2):
        nlist[i], nlist[len(nlist)-i-1] = nlist[len(nlist)-i-1], nlist[i]
    
    for i in nlist:
        print(i,end="")
    print()