n = int(input())

for i in range(n):
    count = 0
    n = input()
    nlist= []
    for i in n:
        if count == 0:
            nlist.append(i.upper())
            count = 1
        else:
            nlist.append(i)

    for i in nlist:
        print(i,end="")
    print()