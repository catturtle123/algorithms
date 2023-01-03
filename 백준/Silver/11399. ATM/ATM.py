n = int(input())

nlist = list(map(int,input().split()))

nlist.sort()

sum = 0
for i in range(n+1,0,-1):
    for j in range(i-1):
        sum += nlist[j]

print(sum)