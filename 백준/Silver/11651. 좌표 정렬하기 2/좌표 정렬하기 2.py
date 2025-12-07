n = int(input())
nlist = []

for i in range(n):
    a, b = map(int, input().split())
    nlist.append((b, a))

nlist.sort()
for b, a in nlist:
    print(a, b)