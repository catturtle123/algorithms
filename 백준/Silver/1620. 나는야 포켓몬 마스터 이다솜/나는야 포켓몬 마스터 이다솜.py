import sys
a,b = map(int,input().split())

plist = []
for i in range(a):
    p = sys.stdin.readline().strip()
    plist.append(p)

pdic = {}
count = 1
for i in plist:
    pdic[i] = count
    count += 1

for i in range(b):
    s = sys.stdin.readline().strip()
    if s.isalpha():
        print(pdic[s])
    else:
        s = int(s)
        print(plist[s-1])

