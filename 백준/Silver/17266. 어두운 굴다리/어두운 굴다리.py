n = int(input())
m = int(input())
nlist = list(map(int,input().split(' ')))

first = nlist[0]
last = n - nlist[m - 1]
height = max(first, last)
for i in range(m - 1):
    height = max((nlist[i + 1] - nlist[i] + 1) // 2 , height)

print(height)