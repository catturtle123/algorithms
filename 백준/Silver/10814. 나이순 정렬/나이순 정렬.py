n = int(input())

o = 0
s = ""
nlist = []
for i in range(n):
    o, s = input().split()
    o = int(o)
    nlist.append((o, s))

nlist.sort(key=lambda x : x[0])

for i in nlist:
     print(f"{i[0]} {i[1]}")