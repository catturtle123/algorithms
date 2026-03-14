nlist = []

for _ in range(4):
    n = int(input())
    nlist.append(n)

if (nlist[0] == 8 or nlist[0] == 9) and (nlist[3] == 8 or nlist[3] == 9) and nlist[1] == nlist[2]:
    print("ignore")
else:
    print("answer")