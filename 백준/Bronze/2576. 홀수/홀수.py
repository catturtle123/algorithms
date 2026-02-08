nlist = []

for _ in range(7):
    n = int(input())
    
    if n % 2 != 0:
        nlist.append(n)

if len(nlist) == 0:
    print(-1)
else:
    print(sum(nlist))
    print(min(nlist))