n = input()
slist = []

while 1:
    try:
        slist.append(n)
        n = input()
    except:
        break

for i in slist:
    print(i)