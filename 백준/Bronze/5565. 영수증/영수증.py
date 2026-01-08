n = int(input())

nlist = []
for _ in range(9):
    s = int(input())
    nlist.append(s)

print(n - sum(nlist))