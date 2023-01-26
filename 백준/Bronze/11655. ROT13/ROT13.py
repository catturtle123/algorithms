n = input()

slist= []
for i in n:
    if i.isalpha():
        snum = ord(i)
        if 65 <= snum <= 90:
            if 90 >= snum + 13:
                slist.append(snum+13)
            else:
                l = snum + 13 - 90 + 64
                slist.append(l)
        if 97 <= snum <= 122:
            if 122 >= snum + 13:
                slist.append(snum+13)
            else:
                l = snum + 13 - 122 + 96
                slist.append(l)
    else:
        slist.append(ord(i))


for i in slist:
    print(chr(i),end="")

