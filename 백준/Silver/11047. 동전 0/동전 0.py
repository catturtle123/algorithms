a,b = map(int,input().split())

nlist = []
for i in range(a):
    num = int(input())
    nlist.append(num)

nlist.sort()
nlist.reverse()

pivot = 0
for i in nlist:
    if i <= b:
        break
    pivot +=1

nlist = nlist[pivot:]

result = 0
result2 = b
for i in nlist:
    result += result2 // i
    result2 = b % i

print(result)