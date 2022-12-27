n = int(input())

sum = 0

nlist = list(map(int,input().split()))

big = max(nlist)

nsum = 0
for i in nlist:
    h = i/big*100
    nsum += h

print(nsum/n)