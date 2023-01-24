n = input()
nlist = []
n = str(n)
for i in n:
    nlist.append(int(i))
nlist.sort()
nlist.reverse()
n = ""
for i in nlist:
    n += str(i)

if n[-1] != "0":
    print(-1)
else:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        n = int(n)
        if n % 3 != 0:
            print(-1)
        else:
            n = int(n)
            print(n)
