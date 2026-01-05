nlist = []

for i in range(4):
    s = int(input())
    nlist.append(s)
    
if sum(nlist) + 300 > 1800:
    print("No")
else:
    print("Yes")