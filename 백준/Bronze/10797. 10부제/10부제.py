n = int(input())
nlist = map(int, input().split())

sums = 0
for i in nlist:
    if n == i:
        sums += 1

print(sums)