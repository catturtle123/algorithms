n = int(input())


for i in range(n):
    count = 0
    nlist = [chr(i) for i in range(65,91)]
    nlist = set(nlist)

    olist = []
    s = input()

    for j in s:
        olist.append(j)
    
    olist = set(olist)

    ulist = nlist - olist

    for j in ulist:
        count += ord(j)
    print(count)

    