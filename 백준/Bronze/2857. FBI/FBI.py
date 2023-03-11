nlist = []
for i in range(5):
    n = input()
    if n.find("FBI") != -1:
        nlist.append(i+1)

if nlist:
    for i in nlist:
        print(i,end=" ")
else:
    print("HE GOT AWAY!")