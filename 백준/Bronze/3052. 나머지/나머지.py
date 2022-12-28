nlist = []
for i in range(10):
    num = int(input())
    nlist.append(num)

plist = []
for i in nlist:
    p = i % 42
    plist.append(p)

sum = 0
for i in range(42):
    u = plist.count(i)
    if u>=2:
        sum += (u-1)

print(10-sum)